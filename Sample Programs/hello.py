from __future__ import print_function
 
import tensorflow as tf
 
hello = tf.constant('Om Namah Shivaya')
 
# Start tf session
sess = tf.Session()
 
# Run the op
print(sess.run(hello))
