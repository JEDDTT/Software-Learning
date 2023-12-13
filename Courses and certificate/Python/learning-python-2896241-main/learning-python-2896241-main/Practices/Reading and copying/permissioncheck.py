import os
def check_file_permissions(file_path):
   if os.access(file_path, os.R_OK):
      print(f"Read permission is granted for file: {file_path}")
   else:
      print(f"Read permission is not granted for file: {file_path}")
    
   if os.access(file_path, os.W_OK):
      print(f"Write permission is granted for file: {file_path}")

   else:
      print(f"Write permission is not granted for file: {file_path}")
    
   if os.access(file_path, os.X_OK):
      print(f"Execute permission is granted for file: {file_path}")
   else:

      print(f"Execute permission is not granted for file: {file_path}")
# Example usage
#file_path2 = os.path.join("C:\Users\HP\Desktop\ReadingCopying")
file_path = "C:\\Users\HP\Desktop\Software-Learning\Courses and certificate\Python\learning-python-2896241-main\learning-python-2896241-main\Practices\Reading and copying"
check_file_permissions(file_path)