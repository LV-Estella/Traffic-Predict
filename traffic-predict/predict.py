from keras.models import load_model
import  numpy as np
model = load_model('C:\\tmp\Traffic\demo_traffic_jam_prediction\model1.h5')
#Tạo input
x0=[0]*55
x0[0]=1
x0[5]=1
x1=[0]*55
x1[49]=1
x1[47]=1
data = np.array([x0,x1])
print(data)
pred= model.predict_classes(data)
print(pred)
pred= model.predict_proba(data)
print(pred)