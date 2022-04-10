"""
File for vehicle count predictions
"""
# For running inference on the TF-Hub module.
import tensorflow as tf

# For drawing onto the image.
import numpy as np
from params_and_keys import *

# Check available GPU devices.
# print("The following GPU devices are available: %s" % tf.test.gpu_device_name())

def model_predict(img_path:str, detector:tf.keras.Model)->dict[str,int]:
    """Predict the counts of the vehicle related objects in the given image"""
    def load_img(path:str)->tf.Tensor:
      """Load and preprocess the image from the given path
      """
      img = tf.io.read_file(path)
      img = tf.image.decode_jpeg(img, channels=3)
      img = tf.image.resize([img], (640, 640))
      img = tf.cast(img, dtype = tf.float32)
      img = img/255
      return img

    def run_detector(detector:tf.keras.Model, path:str)->dict[str,np.array]:
      """Perform predictions using the given object detection model
      """
      img = load_img(path)
      result = detector(img)
      result = {key:value.numpy() for key,value in result.items()}
      return result
    
    def create_counts_dict(thresholds:list = sorted(THRESHOLDS))->dict[str,int]:
      """Create a dictionary for storing counts using the variables
         Stored in the params_and_keys
      """
      car_dict = {car_name+'_'+str(threshold):0 for car_name in CAR_NAMES for threshold in THRESHOLDS}
      return car_dict
  
    
    def get_counts_for_thresholds(thresholds:list = sorted(THRESHOLDS))->dict[str,int]:
      """Extract the vehicle related predictions from the models predictions
      """
      car_dict = create_counts_dict()
      for ind, detection_score in enumerate(img_res.get("detection_scores",[])):
          for threshold in thresholds:
              if detection_score >= threshold:
                  vehicle_type = entities[ind]
                  if vehicle_type in CAR_NAMES:
                      car_dict[vehicle_type+'_'+str(threshold)] += 1
      return car_dict


    img_res = run_detector(detector, img_path)
    entities = []
    for i in img_res.get("detection_class_entities",[]):
      entities.append(i.decode("utf-8"))

    vehicle_counts = get_counts_for_thresholds()
    
    
    return vehicle_counts


