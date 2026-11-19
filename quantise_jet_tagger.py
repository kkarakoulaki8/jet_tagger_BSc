from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
import keras
from keras.layers import  Activation
from keras.callbacks import EarlyStopping, ReduceLROnPlateau

from hgq.layers import QConv1D, QDense, QBatchNormalization, QGlobalAveragePooling1D
from hgq.utils.sugar import FreeEBOPs
from hgq.config import LayerConfigScope, QuantizerConfigScope, QuantizerConfig

def jet_tagger_HGQ(input_shape):
  weight_qconf = QuantizerConfig(
                  q_type="kbi",
                  place="weight",
                  k0=True,            
                  b0=8,  # total bits 
                  i0=4,   # integer bits         
                  overflow_mode="SAT",      
                  round_mode="RND_CONV",
                  trainable=False,
                  )
  
  bias_qconf = QuantizerConfig(
                      q_type="kbi",
                      place="bias",
                      k0=True,           
                      b0=8,           # total bits 
                      i0=4,    # integer bit       
                      overflow_mode="SAT",
                      round_mode="RND_CONV",
                      trainable=False,
                      )
  with QuantizerConfigScope(place='all', default_q_type='kbi', overflow_mode='SAT'):  
    with QuantizerConfigScope(place='datalane', default_q_type='kif',homogeneous_axis=(0,1), overflow_mode='SAT'):
      with LayerConfigScope(enable_ebops=True, heterogeneous_axis=None, beta0=1e-8):
        inputs = keras.layers.Input(shape=input_shape, name='model_input')
        main = QBatchNormalization(name='norm_input')(inputs)
        main = QConv1D(filters=10, kernel_size=1, name='Conv1D_1', activation='relu',use_bias=True,kq_conf=weight_qconf,bq_conf=bias_qconf,iq_conf=None)(main)
        main = QConv1D(filters=10, kernel_size=1, name='Conv1D_2', activation='relu',use_bias=True,kq_conf=weight_qconf,bq_conf=bias_qconf,iq_conf=None)(main)
        main = QGlobalAveragePooling1D(name='avgpool')(main)
        jet_id = QDense(32, name='Dense_1' ,activation='relu',use_bias=True,kq_conf=weight_qconf,bq_conf=bias_qconf,iq_conf=None)(main)
        jet_id = QDense(16, name='Dense_2' ,activation='relu',use_bias=True,kq_conf=weight_qconf,bq_conf=bias_qconf,iq_conf=None)(jet_id)
        jet_id = QDense(8, name='Dense_3' ,activation=None,use_bias=True,kq_conf=weight_qconf,bq_conf=bias_qconf,iq_conf=None)(jet_id)
        jet_id = Activation('softmax', name='jet_id_output')(jet_id)
        jet_model = keras.Model(inputs = [inputs], outputs = [jet_id])
    return jet_model


ebops_tracker = FreeEBOPs()


callbacks = [
            EarlyStopping(monitor='val_loss', patience=10),
            ReduceLROnPlateau(
                monitor='val_loss',
                factor=0.5,
                patience=5,
                min_lr=0.00001,
            ), ebops_tracker
        ]  