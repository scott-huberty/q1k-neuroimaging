.. _vp:

Steady State Visual Evoked Potentials (SSVEP)
=============================================


.. vimeo:: 889675342
    :align: center
    :width: 75%


Overview
--------

The SSVEP task is a visual task that presents 1 second videos of circular random
pattern images alternating between 180º rotated copies at rates of 6Hz or 15Hz. There is
a jittered blank screen of either ``800``, ``900``, ``1000``, ``1100``, or ``1200`` ms
between the offset of the fixation animation and the onset of the stimulus train. A small,
red fixation cross is constantly displayed in the center of the screen throughout the trial.
Before each trial, a small, a fixation animation (throbbing clock) is displayed at the
center of the screen, with the red cross overlaid on top.

Conditions
----------

6Hz
    The circular random pattern images alternate between 180º rotated copies at a
    rate of 6Hz
15Hz
    The circular random pattern images alternate between 180º rotated copies at a
    rate of 15Hz

Blocks / Trials
---------------
The experiment conists of 4 blocks (3 mandatory, 1 optional) of 40 trials each (20 per
condition). If 3 blocks are completed, 120 trials will be completed (60 per condition).
If 4 blocks are completed, 160 trials will be completed (80 per condition).


Animations
----------
Fixation (looming clock)
    At the onset of a trial the fixation is ``0*0px`` and over ``300ms``
    increases in size to ``350*350px`` (looming). Following this the Central
    Stimulus pulses, increasing/decreasing between ``234*234px`` to ``350*350px`` at
    3Hz (throbbing).
Fixation (spinning clock)
    At the onset of a trial the fixation is sized ``234*234px`` and spins
    clockwise at 1.5Hz.
Fixation (throbbing star)
    At the onset of a trial the fixation is ``0*0px`` and over 1 second
    increases in size to ``234*234px`` (throbbing).
Steady state visual evoked stimuli
    A 1-second videos of circular random pattern images alternating between 180º rotated
    copies at rates of 6Hz or 15Hz. The stimuli are 200 pixels wide.


Interest Areas
--------------
An interest area is placed around the SSVEP stimuli, and is used to determine whether
the participant is looking at the stimuli or not, determining whether the trial is
valid or not.


Gaze Triggers
-------------

The SSVEP task does not use gaze any triggers. The stimuli will be presented regardless
of whether the participant made gaze to the stimuli or not. This is out of consideration
for maintaining the steady state of the stimuli. However, eye-tracking data is collected
and can be used assess the validity of trials during offline analyses.

Classifiers
-----------
To aid the researchers running the study with real-time information, classifiers in the
experiment check for certain behaviors required for a valid trial. A trial is deemed
valid if: 

1. Gaze is on stimulus for at least ``600ms`` during the trial.
 
Valid trials are added to a count to the valid sum for that type of trial shown on the
Eyelink Host PC. 

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

========================  ========  ========  =========
Event Description             EGI Event         DIN
------------------------  ------------------  ---------
    Condition               6Hz       15Hz   
========================  ========  ========  =========
Jittered ISI              ``N.A.``  ``N.A.``  
Fixation animation onset  ``fvsr``  ``fvsb``
Jittered ISI              ``N.A.``  ``N.A.``
Onset of 1-second video   ``sv06``  ``sv15``   ``DIN2`` 
========================  ========  ========  =========

In addition to the event codes above, the following codes are also sent to the EGI
Netstation acquisition system, but generally are not needed for offline analysis:

========================  ======================================
Description               EGI Event
------------------------  --------------------------------------
Fixation animation onset  ``fvsr``, ``fvsb``, ``fvct``, ``fvcr``   
begin task                ``VBeg``
Netstation misc event     ``TSYN``
display start menu        ``dstr``
display break menu        ``dbrk`` 
display end screen        ``dend``
========================  ======================================