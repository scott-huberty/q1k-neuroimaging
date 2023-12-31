.. _RS:

Resting-State
==============

.. vimeo:: 889688662
    :align: center
    :width: 75%


Overview
--------

The Resting-State task is meant to measure baseline activity. It consists of 4
different abstract videos that look like screen savers, which play in the centre of the
participant screen. The goal of this is to keep the participant as relaxed as possible,
which is particularly important for young children and some clinical populations Each
video lasts 1 minute, with an opportunity for a break between each video. 

Conditions
----------

There are no conditions defined for this task.

Blocks / Trials
---------------
The experiment consists of 4 blocks, each lasting 1 minute. There is the option of
for additional 5th and 6th blocks, which contains different videos than the first 4 blocks,
and can be used if the experimenter wants to extend the experiment.
 

Animations
----------
Baseline videos
    The baseline videos are akin to screen savers and are present
    throughout the experiment for the participant to view.

Interest Areas
--------------
There are no interest areas defined for this task.


Gaze Triggers
-------------
There are no gaze triggers defined for this task.

Classifiers
-----------
There are no tiral classifiers defined for this task.


Event Messaging
---------------
Experiment Builder will send experiment event codes to both the Eyelink and EGI
acquisition systems, and the event code patterns differ slightly:


EGI acquisition
^^^^^^^^^^^^^^^
EGI Netstation does not support the same event messaging as the Eyelink Host PC, as
event codes are generally restricted to 4 characters. The table below shows the
corresponding event codes for the EGI Netstation acquisition, and the DIN event
triggered by the photo-diode on the screen for each event.


========================  ======================================  ==========
Description               EGI Event                                DIN
------------------------  --------------------------------------  ----------
begin task                ``VBeg``
Display Video             ``vs0[1,2,...,6]``                        ``DIN3``
Netstation misc event     ``TSYN``
display start menu        ``dstr``
display break menu        ``dbrk`` 
display end screen        ``dend``
========================  ======================================  ==========

.. note::
    The integer that is displayed after the ``vs`` event code corresponds to the
    block number, and is incremented by 1 for each block. For example, the first
    block will have the event code ``vs01``, and the second block will have the
    event code ``vs02``.

.. note::
    DIN events represent the onset of each video, and are generated by the Cedrus
    stimtracker photo-dide that is placed on the screen.