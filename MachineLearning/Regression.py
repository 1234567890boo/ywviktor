import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
from mpl_toolkits import mplot3d
import random
import pandas as pd
from sklearn.datasets import load_iris as li
from sklearn import linear_model
from sklearn import metrics
from sklearn.linear_model import LogisticRegression as lr
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler as sc
from sklearn.metrics import confusion_matrix as cmd
from sklearn.metrics import accuracy_score as AS
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets._samples_generator import make_blobs

red=(0,0,255)
green=(0,255,0)
blue=(255,0,0)

#-------------------------------------------------------------------------------------------------------------------
from numpy.lib.npyio import recfromtxt
red=(0,0,255)
green=(0,255,0)
blue=(255,0,0)

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

img1=cv2.imread("test.jpeg",cv2.IMREAD_COLOR)
'''img2=cv2.imread("Bluewall.jpeg",cv2.IMREAD_COLOR)

erodemesh=np.ones((10,10))
erode=cv2.erode(img1,erodemesh)

colorbar=np.zeros((500,500,3),np.uint8)
cbarwinname="color palate"
cv2.namedWindow(cbarwinname)
def cbar():
  pass

cv2.createTrackbar("blue",cbarwinname,0,255,cbar)
cv2.createTrackbar("green",cbarwinname,0,255,cbar)
cv2.createTrackbar("red",cbarwinname,0,255,cbar)

while True:
  cv2_imshow(cbar,colorbar)
  if cv2.waitKey(1)==27:
      break
  blue=cv2.getTrackbarPos("blue",cbarwinname)
  green=cv2.getTrackbarPos("green",cbarwinname)
  red=cv2.getTrackbarPos("red",cbarwinname)
  colorbar[:]=[blue,green,red]
  print(blue,green,red)

border=cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT)

(rows,columns)=(img1.shape[:2])
rotate=cv2.getRotationMatrix2D((columns/2,rows/2),90,1)
rotateimg=cv2.warpAffine(img1,rotate,(rows,columns))

edges=cv2.Canny(img2,100,200)

resize1=cv2.resize(img1,(250,250))
resize2=cv2.resize(img2,(250,250))

#cv2.imwrite("cat2.jpeg",resize1)
#cv2.imwrite("Bluewall2.jpeg",resize2)

subtracted=cv2.subtract(img1,img2,0)
added=cv2.add(img1,img2,0)

#contours,htable=cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#cv2.drawContours(img1,contours,-1,blue,5)

cap=cv2.VideoCapture("sample-mp4-file.mp4")
seperate=cv2.createBackgroundSubtractorMOG2()
while True:
  ret,frame=cap.read()
  fgmask=seperate.apply(frame)
  cv2.waitKey("w")
  cv2_imshow(fgmask)

mask=np.zeros(img1.shape[:2],np.uint8)
bgmodel=np.zeros((1,65),np.float64)
fgmodel=np.zeros((1,65),np.float64)
rec=(100,100,100,100)
cv2.grabCut(img1,mask,rec,bgmodel,fgmodel,3,cv2.GC_INIT_WITH_RECT)
mask2=np.where((mask==2)|(mask==0),0,1).astype("uint8")
newimg=img1*mask2[:,:,np.newaxis]
cv2_imshow(newimg)


if __name__ == '__main__' :
  img1=cv2.imread("cat.jpeg",cv2.IMREAD_COLOR)
  r = cv2.selectROI(img1)
  imCrop = img1[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
  cv2.imshow("r",imCrop)
  cv2.waitKey(0)

height=350
width=350
#img=np.zeros((height,width,3))

line=cv2.line(img1,(0,100),(75,100),green,5)

arrow=cv2.arrowedLine(img1,(0,50),(75,50),green,5,tipLength=0.1) #tipLenght can be 0-1

ellipe=cv2.ellipse(img1,(150,150),(25,5),30,360,0,red,2)

circle=cv2.circle(img1,(150,100),25,red,2)

rect=cv2.rectangle(img1,(150,10),(100,50),red,2)

text=cv2.putText(img1,'CV',(250,50),cv2.FONT_HERSHEY_SIMPLEX,1,red,3)

centroid1=(350,200)
centroid2=(300,250)
centroid3=(250,150)
centroid=((centroid1[0]+centroid2[0]+centroid3[0])//3,(centroid1[1]+centroid2[1]+centroid3[1])//3)

centroidline1=cv2.line(img1,centroid1,centroid2,red,2)
centroidline2=cv2.line(img1,centroid2,centroid3,red,2)
centroidline3=cv2.line(img1,centroid3,centroid1,red,2)
centroidDraw=cv2.circle(img1,centroid,5,red,2)


r,g,b=cv2.split(img1)
gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
hsv=cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)

lowerhsv=np.array([60,35,140])
upperhsv=np.array([180,255,255])
hsvmask=cv2.inRange(hsv,lowerhsv,upperhsv)
final=cv2.bitwise_and(img1,hsvmask,mask=hsvmask)

edges=cv2.Canny(gray,width,height)
cv2.waitKey(0)

cv2_imshow(erode)
cv2.imwrite("newimg.jpeg",g)
#use r,g,b for img for single color/grayscale or full img


shrink=img1.copy()
for n in range(0,4,1):
  shrink=cv2.pyrDown(shrink)
  cv2_imshow(shrink)
  cv2.waitKey(0)'''


hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
min_color = np.array([0, 0, 0])
max_color = np.array([100, 100, 255])
mask = cv2.inRange(hsv, min_color, max_color)
res = cv2.bitwise_and(img1, hsv, mask)

cv2_imshow(img1)
cv2_imshow(hsv)
cv2_imshow(mask)
cv2_imshow(res)


cv2.waitKey(0)
cv2.destroyAllWindows()
#-------------------------------------------------------------------------------------------------------------------
red=(0,0,255)
green=(0,255,0)
blue=(255,0,0)

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

img1 = cv2.imread("Blue.png", cv2.IMREAD_COLOR)
img2 = cv2.imread("Red.png", cv2.IMREAD_COLOR)

grayimg1 = cv2.imread("Blue.png", cv2.IMREAD_GRAYSCALE)
grayimg2 = cv2.imread("Red.png", cv2.IMREAD_GRAYSCALE)

grayface = cv2.imread("Face.png", cv2.IMREAD_GRAYSCALE)

# -------------------------------------------------------------------------------------------------------------------
'''hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
min_color = np.array([111, 111, 138])
max_color = np.array([113, 179, 156])
mask = cv2.inRange(hsv, min_color, max_color)
res = cv2.bitwise_and(img1, img1, mask)
contour_frame=mask.copy()
contours,hierachy=cv2.findContours(contour_frame,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
sorted_contours=sorted(contours, key=cv2.contourArea, reverse=True)
edges=cv2.Canny(img1,30,200)
cv2.drawContours(contour_frame,contours,-1,(0,0,0))
cv2_imshow(contour_frame)
cv2_imshow(mask)'''
# -------------------------------------------------------------------------------------------------------------------
'''
gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
sift=cv2.xfeatures2d.SIFT_create
kp=sift.detect(gray)
kp,des=sift.compute(gray)
cv2.drawKeypoints'''
# -------------------------------------------------------------------------------------------------------------------
'''
cv2_imshow(img1)
gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
fast=cv2.FastFeatureDetector_create()
brief=cv2.xfeatures2d.BriefDescriptorExtractor_create()
kp=fast.detect(img1)
kp1,des=brief.compute(img1,None)
keypoints_img=cv2.drawKeypoints(gray,kp,img1,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2_imshow(keypoints_img)'''
# -------------------------------------------------------------------------------------------------------------------

'''detect=cv2.ORB_create()
kp1,des1=detect.detectAndCompute(img1,None)
kp2,des2=detect.detectAndCompute(img2,None)
bf_matcher=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
num_of_matches=bf_matcher.match(des1,des2)

def drawMach(kp1,kp2,matches):
  outputimg=cv2.drawMatches(img1,kp1,img2,kp2,matches,None,flags=2)
  #outputimg2=cv2.drawMatches(img2,kp1,img1,kp2,matches,None,flags=2)

  coords2 = [kp2[match2.trainIdx].pt for match2 in matches]
  trueaveragex=0
  trueaveragey=0
  for n in range(0,len(coords2),1):
    averagex=coords2[n][0]
    averagey=coords2[n][1]
    trueaveragex+=averagex
    trueaveragey+=averagey
  trueaveragex/=len(coords2)
  trueaveragey/=len(coords2)

  circleimg=cv2.circle(outputimg,(int(trueaveragex),int(trueaveragey)),10,red,2)
  #circleimg2=cv2.circle(outputimg2,(int(trueaveragex),int(trueaveragey)),10,red,2)

  #trueoutimg=circleimg2+circleimg

  cv2_imshow(circleimg)

drawMach(kp1,kp2,num_of_matches)'''
# -------------------------------------------------------------------------------------------------------------------

face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "Haar_Cascades.xml")

faces = face_cascades.detectMultiScale(grayface, 1.3, 5)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.waitKey(0)
cv2.destroyAllWindows()
#=========================================================================================================

'''x,y=make_blobs(n_samples=500,centers=5,random_state=0,cluster_std=0.40)

plt.scatter(x[:,0],x[:, 1],c=y,s=50,cmap='Accent')
plt.show()

#=========================================================================================================

li=li()

x=li.data
y=li.target

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=.4,random_state=1)
gnb=GaussianNB()
gnb.fit(xtrain,ytrain)

ypredict=gnb.predict(xtest)

print(metrics.accuracy_score(ytest,ypredict)*100)
print(ypredict)

#=========================================================================================================

'barwidth=0.25
subject1=[40,1,25,10,27]
subject2=[25,12,13,18,19]
subject3=[23,36,18,15,14]

bar1=np.arange(len(subject1))
bar2=[x+barwidth for x in bar1]
bar3=[x+barwidth for x in bar2]

plt.bar(bar1,subject1,color="blue",width=barwidth,label="subject1")
plt.bar(bar2,subject2,color="green",width=barwidth,label="subject2")
plt.bar(bar3,subject3,color="red",width=barwidth,label="subject3")
plt.xticks([y+barwidth for y in range(0,len(subject1),1)],['2010','2011','2012','2013','2014'])
plt.xlabel("Subjects",fontweight="bold",fontsize=17)
plt.ylabel("Percentage",fontweight="bold",fontsize=17)
plt.legend()
plt.show()

#=========================================================================================================

data=pd.read_csv('RegressionWithCSVBank.csv')

x=data.iloc[:,[2,3]].values
y=data.iloc[:,[4]].values

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.20,random_state=0)

sc_x=sc()
sc_y=sc()

xtrain=sc_x.fit_transform(xtrain)
xtest=sc_x.fit_transform(xtest)

lr_xy=lr(random_state=0)
lr_xy.fit(xtrain,ytrain)

y_pred=lr_xy.predict(xtest)
cm=cmd(ytest,y_pred)
#[[true positive,false positive][true negative,false negative]]
print(AS(ytest,y_pred))


#=========================================================================================================

x=np.outer(np.linspace(-1,1,25),np.ones(25))
y=x.copy().T
z=np.sin(x*3-y*2)

fig=plt.figure()
tdproj=plt.axes(projection="3d")

#tdproj.plot_surface(x,y,z,cmap="viridis",edgecolor="blue") #Terrain
#tdproj.plot_wireframe(x,y,z,color="blue") #Wireframe
#tdproj.contour3D(x,y,z,cmap="viridis") #Contour
tdproj.scatter3D(x,y,z,color="blue") #Scatter Plot

plt.show()

#=========================================================================================================

def wf(x,y):
    return np.sin(np.sqrt(x**2++y**2))

x=np.linspace(-1,5,10)
y=np.linspace(-1,5,10)
X,Y=np.meshgrid(x,y)
Z=wf(X,Y)

fig=plt.figure()
tdproj=plt.axes(projection="3d")

tdproj.plot_wireframe(X,Y,Z,color="blue")
plt.show()

#=========================================================================================================

fig=plt.figure()
tdproj=plt.axes(projection="3d")

z=np.linspace(0,1,100)
x=z*np.sin(z) #can be sin tas or cos
y=x*np.tan(x) #can be sin tas or cos
c=x+y

tdproj.plot3D(x,y,z,"c")
plt.show()

#=========================================================================================================

np.random.seed(2)
x=np.random.normal(3,1,100)
y=np.random.normal(200,50,100)/x


train_x=x[:80]
train_y=y[:80]
test_x=x[80:]
test_y=y[80:]

line=np.linspace(0,6,100)
polynomialmodel=np.poly1d(np.polyfit(train_x,train_y,4))

r2=r2_score(test_y,polynomialmodel(test_x))
print(r2)

plt.scatter(test_x,test_y)
plt.plot(line,polynomialmodel(line))
plt.show()

#=========================================================================================================

df=pd.read_csv("RegressionWithCSV.csv")
x=df[["Volume","Weight"]]
y=df["CO2"]

linemodel=linear_model.LinearRegression()
linemodel.fit(x,y)
predictedCo2=linemodel.predict([[200,1]])
print(predictedCo2)

#=========================================================================================================

x=[80,43,36,36,95,10,66,34,37,20,26,29,48,64,6,5,36,66,72,42]
y=[20,46,3,35,67,95,51,72,58,10,26,34,90,33,38,20,56,2,47,16]

slope,intercept,r,p,std_err=stats.linregress(x,y)

def slopefinder(x):
    return slope*x+intercept

model=list(map(slopefinder,x))

line=np.linspace(min(x),max(x),max(y))

plt.scatter(x,y)
plt.plot(line,model(line))
plt.show()

polynomialmodel=np.poly1d(np.polyfit(x,y,3))

print(r2_score(y,polynomialmodel(x)))
#---------------------------------------------------------------------------------------------------------#

rand=random.randint(min(x),max(x))
polynomialmodel=np.poly1d(np.polyfit(x,y,3))
speed=polynomialmodel(rand)
print(speed,rand)

line=np.linspace(min(x),max(x),max(y))
plt.scatter(x,y)
plt.plot(line,polynomialmodel(line))
plt.show()'''