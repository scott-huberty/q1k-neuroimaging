.. _VS:

Visual Search (VS)
==================

.. _VS-image:

.. figure:: https://raw.githubusercontent.com/scott-huberty/Q1K-doc-assets/main/_images/task_images/Q1K-Visual-Search.png
    :alt: Image of Visual Search task, showing the stimuli and interest areas
    :align: center

    Visual search stimuli with interest area sizing and white search array constrain

Overview
--------

The Visual Search task measures mean reaction time to find a target amongst distractors. 
A target (red-apple) flys from a randomly selected corner of the screen into a random 
location within the circular array, where there are distractors (red apple slices, and/or
whole blue apples).  Trials vary between 5, 9, or 13 total distractors, and between 1 or 
2 types of distractors (red apple slices, blue whole apples, or both). When the participant
gazes to the target (red whole apple), the apple rotates and an applause is played. 
The target red apple and the distractors are blue apple are both ``180*180px`` (3.1*3.1o) images,
and the red apple slice is ``45*270px`` (0.8*4.6o), as shown in Figure 3. When the participant 
gazes to the target (red whole apple), the apple rotates and an applause is played.


.. vimeo:: 876494648
    :align: center
    :width: 75%

Conditions
----------

Mismatch type 

Colour mismatch
    Whole red apple amongst whole blue apples
Slice mismatch
    Whole red apple amongst red apple slice
Conjunction mismatch
    Whole red apple amongst whole blue apples and red apple slices
Number of distractors
    5, 9 or 13 distractors

Interest Areas
--------------

The interest areas for the apples are ``220px`` in diameter. They are this small in order
to have non-overlapping interest areas. The apple slice interest areas are ``65*290px``, 
note that the 0 and 12 IA locations do overlap substantially, so there are no trials with 
both 0 and 12 location apple slice distractors. There are interest areas for all displayed 
images including the distractors. This may be informative to analyze eye movements to 
distractor features as a factor. 

Gaze Triggers
-------------

The two gaze triggers in this experiment are low latency invisible boundary triggers.
The minimum duration for the fly-in apple and the target apple gaze triggers are both 
``50ms``. As with the Gap overlap task, the reaction time for the search time is taken 
from the first sample within the invisible boundary that fired (50ms later). 


Classifiers
-----------
A trial is deemed valid if the search target IB trigger fires producing an RT value.
There experiment plays until the participant completes 26 valid trials. If the 
participant does not gaze to the target apple within ``2000ms``, the trial is recycled.
If the participant does not complete 26 valid trials within 48 trials, the experiment 
ends.

Animations
----------
Each trial begins with a red target apple (``180*180px``) which flies from either 
the top left or right corners over ``750ms``. It then remains in the center of the 
screen with a ``220px`` diameter interest area, until gaze is within the interest 
area region for ``50ms`` or ``2000ms`` elapses (the trial is immediately recycled,
and the attention getter is shown). All trials that show a search array present a
reward animation, which is the target apple rotating clockwise 180 degrees for 
``500ms`` then anti-clockwise 180 degrees (returning upright) for ``750ms``.

Event Messaging
---------------

Each trial begins with the message ``APPLE_FLY_IN`` and is followed by
``GAZE_TO_ATTENTION_APPLE`` (or ``NO_GAZE_TO_APPLE`` after the 2000ms timeout). When
the fixation image is shown, the message ``DISPLAY_FIXATION`` is written and after
750ms delay the message ``DISPLAY_SEARCH`` is written. If the participant’s gaze triggers 
the target IA, ``GAZE_TO_TARGET`` is written (or ``TIMEOUT`` if not after 4000ms). When
the reward animation begins ``DISPLAY_REWARD`` is written, and the trial ends with 
``DISPLAY_BLANK`` when the final blank screen is displayed. 

EGI acquisition
^^^^^^^^^^^^^^^
EGI Netstation does not support the same event messaging as the Eyelink Host PC, as
event codes are generally restricted to 4 characters. The table below shows the
corresponding event codes for the EGI Netstation acquisition, and the DIN event
triggered by the photo-diode on the screen for each event.


+-------------------------+--------+--------+------+--------+--------+------+--------+--------+------+---------------+-------------------+
| Event Marker            |      Red Apple Slices  | Blue Whole Apples      |   Conjunction          | DIN Event EGI | DIN Event EYELINK |
+=========================+========+========+======+========+========+======+========+========+======+===============+===================+
| APPLE_FLY_IN            |  **5** |  **9** |**13**|  **5** |  **9** |**13**|  **5** |  **9** |**13**|    DIN3       |        4          |
|                         +--------+--------+------+--------+--------+------+--------+--------+------+               |                   |
|                         | da5s   | da9s   | datc | da5a   | da9a   | datc | da5c   | da9c   | datc |               |                   |
+-------------------------+--------+--------+------+--------+--------+------+--------+--------+------+---------------+-------------------+
| GAZE_TO_ATTENTION_APPLE |**5**   |**9**   |**13**|**5**   |**9**   |**13**|**5**   |**9**   |**13**|                                   |                  
|                         +--------+--------+------+--------+--------+------+--------+--------+------+                                   |
|                         | ga5s   | ga9s   | gatc | ga5a   | ga9a   | gatc | ga5a   | ga9a   | gatc |                                   |
+-------------------------+--------+--------+------+--------+--------+------+--------+--------+------+---------------+-------------------+
| NO_GAZE_TO_APPLE        |                                                                                                              |       
|                         |                                                                                                              |       
|                         |                                                                                                              |   
+-------------------------+--------+--------+------+--------+--------+------+--------+--------+------+---------------+-------------------+
| DISPLAY_FIXATION        |**5**   |**9**   |**13**|**5**   |**9**   |**13**|**5**   |**9**   |**13**|      DIN2     |       2           |
|                         +--------+--------+------+--------+--------+------+--------+--------+------+               |                   |
|                         |  df5s  |  df9s  | dftc |  df5a  |  df9a  | dftc | df5c   | df9c   | dftc |               |                   |
+-------------------------+--------+--------+------+--------+--------+------+--------+--------+------+---------------+-------------------+
| DISPLAY_SEARCH          |**5**   |**9**   |**13**|**5**   |**9**   |**13**|**5**   |**9**   |**13**|    DIN3       |      4            |
|                         +--------+--------+------+--------+--------+------+--------+--------+------+               |                   |
|                         | ds5s   | ds9s   | dstc | ds5a   | ds9a   | dstc | ds5c   | ds9c   | dstc |               |                   | 
+-------------------------+--------+--------+------+--------+--------+------+--------+--------+------+---------------+-------------------+
| GAZE_TO_TARGET          |**5**   |**9**   |**13**|**5**   |**9**   |**13**|**5**   |**9**   |**13**|                                   |   
|                         +--------+--------+------+--------+--------+------+--------+--------+------+                                   |    
|                         | gt5s   | gt9s   | gttc | gt5a   | gt9a   | gttc | gt5c   | gt9c   | gttc |                                   |
+-------------------------+--------+--------+------+--------+--------+------+--------+--------+------+---------------+-------------------+
| TIMEOUT                 |                                                                                                              | 
|                         |                                                                                                              |
|                         |                                                                                                              |
+-------------------------+--------+--------+------+--------+--------+------+--------+--------+------+---------------+-------------------+
| DISPLAY_REWARD          |**5**   |**9**   |**13**|**5**   |**9**   |**13**|**5**   |**9**   |**13**|     DIN2      |        2          |
|                         +--------+--------+------+--------+--------+------+--------+--------+------+               |                   |
|                         | dr5s   | dr9s   | drtc | dr5a   | dr9a   | drtc | dr5c   | dr9c   | drtc |               |                   |
+-------------------------+--------+--------+------+--------+--------+------+--------+--------+------+---------------+-------------------+
| DISPLAY_BLANK           |**5**   |**9**   |**13**|**5**   |**9**   |**13**|**5**   |**9**   |**13**|                                   |
|                         +--------+--------+------+--------+--------+------+--------+--------+------+                                   |
|                         | db5s   | db9s   | dbtc | db5a   | db9a   | dbtc | db5c   | db9c   | dbtc |                                   |
+-------------------------+--------+--------+------+--------+--------+------+--------+--------+------+---------------+-------------------+

