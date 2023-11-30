.. _AS:

Anti-Saccade (AS)
=================

.. _AS-image:

.. figure:: https://raw.githubusercontent.com/scott-huberty/Q1K-doc-assets/main/_images/task_images/Q1K-Anti-Saccade.png
    :alt: Image of the Anti-Saccade task, showing the stimuli and interest areas
    :align: center

    Anti-Saccade and interest area placement and sizing.

Overview
--------

The Anti-Saccade task has been widely used to examine saccadic movements and inhibitory
control and attention in clinical populations.Each trial begins with the presentation of one
of the four (randomly selected) fixation starts sized at ``175*175px``. Then, a black dot 
(distractor) is presented after the participants have fixed their gaze on one of the randomly
selected central fixations. The distractor is ``175*175px`` and is presented ``803px`` to the
left or the right of screen center. After 1000ms, a red target is presented on the opposite side.
The target red dot is ``234*234px``, and after the participants have looked at it, is replaced 
by a random selection from the four reward animations, which are also ``234*234px``. The goal 
of the task is to look at the target as quickly as possible.

.. vimeo:: 877645510
    :align: center
    :width: 75%

Conditions
----------

Pro-saccade
    Participant's gaze to distractor, then gaze to the
    target >100ms or more after its onset 
Corrective Saccade
    Participant's gaze to distractorm then gaze to the
    target before or within 100ms of its presentation.
Anti-Saccade
    No gaze to distractor, gaze to target before or within
    100ms of its presentation. 


.. note::
    All conditions are defined by the participants own gaze beahviour and the critical period of
    behaviour is from the onset of the distractor until the onset of the targe image (except for
    the "Anti-saccade condition")

Interest Areas
--------------

The fixation star, the distractor black dot and the target side (and red dot) each have 
an elliptical ``450px`` interest area (IA).


Gaze Triggers
-------------

The trials begin with an invisible boundary (IB) trigger around the fixation star animation,
which fires when gaze is held within the ``450px`` diameter IA (``500ms`` minimum duration).
This trigger onsets the distractor image (block dot), which is on screen for ``200ms``. 
When the distractor image is shown, as well as when the following ``1000ms`` period during
which only the background image is shown prior to the target image, there are IB triggers 
around both the distractor dot and target location. There is ``0ms`` minimum duration on 
the distractor side IB (so that gaze to this side can be quickly identified without 
interrupting potential corrective saccades). The target side saccades, which directly 
trigger the reward animation have a minimum duration of 50ms (to ensure no misclassification
or saccades that are not held within the IA region). Finally, when the target red dot is shown,
there is a 0 IB trigger with a 0ms minimum duration that will fire immediately. 

Classifiers
-----------
First, a Boolean (true/false) variable ``DISTRACTOR_SACCADE`` (DS) for whether gaze was 
detected to the distractor IA during its presentation (``200ms``) or the following ``100ms``.
Second, if the first is true, a variable ``AS_DISTRACTOR_SAC_RT`` is updated with a reaction
time to the distractor from its onset to the first sample of the triggering gaze behavior.
Note that, if the first Boolean is false the second RT measure will be the default -1 value.
Third, a Boolean variable ``PREDICTIVE_SACCADE`` (PS) is updated to TRUE if gaze is detected
to the target side either before the onset of the target, or within ``100ms`` of the target 
onset. The fourth variable is ``AS_TARGET_SAC_RT`` is a reaction time measure formed of the
difference between the first sample to the target IA and the onset of the distractor dot,
this RT variable is also updated if the gaze triggers after the target onset (``+100ms``).
With this information some conditional triggers determine whether the trial is either an 
anti-saccade, pro-saccade or corrective saccade. Below is a summary of trial labels: 


1. Pro-saccade: Contains a true DS variable and a false PS variable.
2. Corrective saccade: Contains a true DS variable and a true PS variable.
3. Anti-saccade: Contains a false DS variable and a true PS variable. 
  

Trials that do not meet these conditions, e.g. gaze only to the fixation star then the target
after presentation, are deemed invalid. 

Animations
----------
Fixation (start)
    A fixation star throbs, changing in size between 50% and 100% at 1.5Hz.
Reward Animation (start)
    The reward  animations shrink to 75% whilst rotating 45 clockwise for ``500ms`` then return to 
    100% centered over ``500ms``. They then shrink 75% and rotate anticlockwise for ``500ms``
    returning to 100% and centered. The duration of the reward animation is ``2500ms``.

Event Messaging
---------------

Because the task is designed to be run on both the Eyelink and EGI acquisition systems,
Experiment Builder will send experiment messages to both systems. The messages sent to
the Eyelink Host PC and to the EGI Netstation acquisition will differ slightly.

Eyelink
^^^^^^^


Fixation Onset
    The trial begins with the message ``DISPLAY_FIXATION`` (onset of the star), followed by
    either ``GAZE_TO_FIX`` or ``TRIAL_TIMEOUT``(if not gaze within ``2500ms``).
Distractor Onset (black dot)
    When the distractor is shown (black dot), ``ONSET_DISTRACTOR`` is written. If
    the participant does not gaze to the target side after ``200ms`` of the distractor onset, the
    distractor will disappear and the message ``DISTRACTOR_OFFSET``is written. If the participant gazes
    directly to the distractor after its onset, or within ``200ms`` of its offset, ``GAZE_TO_DISTRACTOR``
    is written. 
Target Onset (red dot)
    If the participant gazes directly to the target side *before* it onsets, *or* within ``100ms`` of its onset,
    then ``PREDICT_TARGET_GAZE`` is written. If the participant gazes to the target side
    after ``100ms`` of the target onset, then ``GAZE_TO_TARGET`` is written. If the
    participant does not gaze to the target side within ``1000ms``of the target onset,
    ``TARGET_ONSET`` is written when the target is displayed. If no gaze is detected to
    the target side, ``TRIAL_TIMEOUT`` is written.
Reward Animation (star)    
    When the reward animation is shown, the message ``"REWARD_ONSET"`` is written
    followed by ``TRIAL_END``.
Trial Classification
    The final message of the trial writes the result of the
    classifier (e.g, ``"PRO_SACCADE"``, ``"CORRECTIVE_SACCADE"``, ``"ANTI_SACCADE"`` etc.).


EGI acquisition
^^^^^^^^^^^^^^^
EGI Netstation does not support the same event messaging as the Eyelink Host PC, as
event codes are generally restricted to 4 characters. The table below shows the
corresponding event codes for the EGI Netstation acquisition, and the DIN event
triggered by the photo-diode on the screen for each event.

=========================  ========  ========  ========
Eyelink Event                 EGI Event         DIN
-------------------------  ------------------  --------
    Condition              Left      Right
=========================  ========  ========  ========    
``"DISPLAY_FIXATION"``      dfxl      dfxr      DIN3 
``"GAZE_TO_FIX"``           gfxl      gfxr     ``N.A.``
``"ONSET_DISTRACTOR"``      ddtl      ddtr      DIN2
``"GAZE_TO_DISTRACTOR"``    gddl      gddr     ``N.A.``
``"PREDICT_TARGET_GAZE"``   gdtl      gdtr     ``N.A.``
``"DISTRACTOR_OFFSET"``     dbgl      dbgr     ``N.A.``
``"TARGET_ONSET"``          dtgl      dtgr      DIN2
``"GAZE_TO_TARGET"``        gttl      gttr     ``N.A.``
``"REWARD_ONSET"``          drwl      drwl      DIN3
``"TRIAL_TIMEOUT"``         N.A.      N.A.      N.A.
``"TRIAL_END"``             N.A.      N.A.      N.A.
=========================  ========  ========  ========





.. note::
    In addition to the event codes above, the following codes are also sent to the EGI
    Netstation acquisition system, but they don't contain a corresponding Eyelink event:
    If the distractor offsets, and the participant gaze is on the distractor side ``gbdl``
    or ``gbdr`` are written, corresponding to whether the distractor was on the left
    or right side of the screen. Alternatively if the participant looked to the *target*
    side *after* the distractor disappears, then ``gbtl`` or ``gbtr`` are written, again
    corresponding to the side of the screen that the *target* is on.