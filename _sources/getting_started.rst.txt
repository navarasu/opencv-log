Logging \\ Debuging
===================

.. code-block:: python

   import cvlog as log
   import cv2

   # image read using opencv

   img = cv2.imread("sample.png")

   # Based on the log mode, the below line
   # 1. Log the image to html (LOG mode) or
   # 2. Show the image using cv2.imshow (DEBUG mode) or
   # 3. Do Nothing (NONE mode)

   log.image(log.Level.ERROR, img)
   
We can run this file ``log_example.py`` with three modes,

Run in Log mode
###############
.. code-block:: sh

   CVLOG_MODE=LOG  python logging_example.py

This creates the image a interaractive html file ``log\log.html``

.. image:: https://user-images.githubusercontent.com/20145075/69906004-ba752f00-13e2-11ea-8714-2425202148e8.png
   :height: 350px

Run in Debug mode
#################
.. code-block:: sh

   CVLOG_MODE=LOG  python logging_example.py

This shows the image using ``cv2.imshow()``

.. image:: https://user-images.githubusercontent.com/20145075/78092636-e2ef5300-73ed-11ea-80f7-3a496388cc3d.png
   :height: 300px

Run in None\\OFF mode
#####################

.. code-block:: sh

   python logging_example.py

This neither logs the image nor shows the image. 

Testing Reporting
=================

It is a semi automated and it automates only the reporting part. 
The validation part is done manually and we need to report the result by pressing 'y' or 'n' key.

**What it does?**

This shows processed output image using cv2.imshow that need to verified.

* On presssing 'y' key, it report it as PASS
* On pressing any other key, it report it as FAIL and save output image for verification
* On any exception, it report it as ERROR with exception stack

It generates CSV ot HTML report which can be used to for accuracy analysis.
By combining the log and test reporting, we can generate an interaractive html to debug and analyse the issue offline.

.. todo:: 
    HTML reporting is in milestone and it will be added in 1.4.0 version.


.. code-block:: python

   import cvtest as test
   import cv2

   # Example Process Image method from image path
   def process_image(imagepath):
      if imagepath == "error.png":
         raise Exception("Some exception in processing image")
      img = cv2.imread(imagepath)
      return img

   # List of the images path to be tested
   test_image_paths=["example1.png","example1.png","error.png"]

   # Run the test
   test.report(test_image_paths, process_image)
