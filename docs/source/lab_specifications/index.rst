.. _lab-specification:

Q1K EEG-eyetracking Lab Specification
=====================================

This section describes the hardware and software, and lab configurations for the Q1K
EEG-eyetracking lab. Provided that you have access to the same hardware and software,
you can use this documentation to replicate the Q1K EEG-eyetracking lab setup.



Overview
--------
Simultaneously recorded eye tracking (ET) and EEG require the two recordings to be synchronized
in time. In the Q1K set-up, the ET and EEG are recorded on separate computers, but 
both systems receive the same trigger signal (i.e. events) from the stimulus computer,
which is used to synchronize the two recordings during analysis. 

The Q1k lab uses Magstim (EGI) EEG equipment and SR Research ET equipment. The
EGI system is comprised of a Mac computer running Net Station 5, and a Net Amps 400 EEG
amplifier. The SR Research system is comprised of a PC running the experiment software
and an Eyelink 1000 Plus eye tracker (which itself is comprised of a standalone PC, which
we call the "Host PC", and the eye tracking lens on A participant display).


.. figure:: https://raw.githubusercontent.com/scott-huberty/Q1K-doc-assets/main/_images/lab/eeg-Setup.jpg
    :alt: blueprint layout of the EEG-Eyetracking setup
    :align: center

Hardware
--------

+-------------------------+-------------------------+-------------------------+
|        Hardware         |       Software          |     Specifications      |
+=========================+=========================+=========================+
| EGI Net Amps 400        |                         |                         |
+-------------------------+-------------------------+-------------------------+
| EGI 129ch Hydrocel Nets |                         |                         |
+-------------------------+-------------------------+-------------------------+
| Cedrus Stimtracker      | - Xidon 2               | - M-Pod for EGI         |
|                         | - Firmware 2.2.7        |   Firmware 2.2.7        |
|                         |                         | - M-POD for parallel    |
|                         |                         |   port firmware 2.2.2   |
+-------------------------+-------------------------+-------------------------+
| iMac                    | Net Station 5           | - 27 inch display.      |
|                         | Acquisition software    | - OSX 10.13.4           |
|                         |                         | - 2 GHz Intel Core 2 Duo|
|                         |                         | - 16 RAM                |
|                         |                         | - Acquisition sampling  |
|                         |                         |   rate: 1000Hz          |
+-------------------------+-------------------------+-------------------------+
| SR Research Eyetracker  |                         | - sampling rate: 1000Hz |
| "Host" PC               |                         | - 32ºx25º trackable     |
|                         |                         |   area                  |
|                         |                         | - 16mm lens             |
|                         |                         | - 0.05º RMS             |
|                         |                         | - 0.25º saccade         |
|                         |                         |   resolution            |
+-------------------------+-------------------------+-------------------------+
| Experiment software     | - Experiment Builder    |                         |
| Ultra Performance PC    |   2.2.299               |                         |
| ("Display PC")          | - DataViewer            |                         |
|                         | - Windows 10 64-Bit     |                         |
+-------------------------+-------------------------+-------------------------+
| ASUS VG248QE, 24”       |                         | 1920 x 1080 resolution  |
| Participant Display     |                         |                         |
+-------------------------+-------------------------+-------------------------+




Communication Across systems
----------------------------
The Display PC, Host PC, iMac (Net Station Acquisition), and EEG amplifier are all connected
to a ethernet HUB via ethernet cables, which allows them to communicate with each other and
share events. The specific communication protocol is handled under the hood by the Magstim and 
SR software, as these two companies maintain an ongoing collaboration to ensure that their
systems are compatible.

Cedrus Stimtracker
------------------

The Cedrus Stimtracker is a device that measures the actual times of stimulus presentation
(both visual and auditory) and sends this information back to the EEG and eyetracking 
acquisition systems. This information is critical for synchronizing the EEG and ET data, 
as the cedrus events regarding stimulus onsets are used to synchronize the EEG and ET data.

Configuring the Stimtracker
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The Stimtracker can be configured via a combination of the knobs on the device itself, and
the Xidon 2 software. The knobs on the device are used to set the sensitivity of each
line (Light sensor 1, Light sensor 2, Audio left, Audio right), and the Xidon 2 software
can be used to specify further device settings, such as hold on/off times, and to set
specific settings for each M-Pod connected to the Stimtracker.

+--------------------------+--------------------------+--------------------------+
|        Trigger           |       Placement          |     Specifications       |
+==========================+==========================+==========================+
| Light Sensor 1           | - Top-Left Corner        | - Sensitivity: 12        |
| (photocel 1)             |   of participant display | - Hold on: 0 ms          |
|                          |                          | - Hold off: 0 ms         |
|                          |                          | - Single-shot: disabled  |
+--------------------------+--------------------------+--------------------------+
| Light Sensor 2           | - Directly to the right  | - Sensitivity: 12        |
| (photocel 2)             |   of Photocel 1          | - Hold on: 0 ms          |
|                          |                          | - Hold off: 0ms          |
|                          |                          | - Single-shot: disabled  |
+--------------------------+--------------------------+--------------------------+
| Audio left               | - Aux port of Display PC | - Sensitivity: 30        |
|                          |   to Audio-in Port of    | - Hold on: 0 ms          |
|                          |   Stimtracker            | - Hold off: 0 ms         |
|                          | - Stimtracker            | - Single-shot: disabled  |
|                          |   Audio-out port to      |                          |
|                          |   speakers (aux cord)    |                          |
+--------------------------+--------------------------+--------------------------+
| Audio right              | - Aux port of Display PC |  - Sensitivity: 30       |
|                          |   to Audio-in Port of    |  - Hold on: 0 m          |
|                          |   Stimtracker            |  - Hold off: 0 ms        |
|                          | - Stimtracker            |  - Single-shot: disabled |
|                          |   Audio-out port to      |                          |
|                          |   speakers (aux cord)    |                          |
+--------------------------+--------------------------+--------------------------+
| M-Pod Parallel port      | - Connected to Parallel  | - Logic: Positive        |
|                          |   port of host PC        | - Output Mode: Reflective|
|                          |                          | - Pulse Duration: 0 ms   |
|                          |                          | - Line 1: Light Sensor 1 |
|                          |                          | - Line 2: Light Sensor 2 |
|                          |                          | - Line 3: Audio Left     |
|                          |                          | - Line 4: Audio Right    |
+--------------------------+--------------------------+--------------------------+
| M-Pod EGI                | - Connected to EGI Amp   | - Logic: Negative        |
|                          |   parallel port 1-8      | - Output Mode: Reflective|
|                          |                          | - Pulse Duration: 0 ms   |
|                          |                          | - Line 1: Light Sensor 1 |
|                          |                          | - Line 2: Light Sensor 2 |
|                          |                          | - Line 3: Audio Left     |
|                          |                          | - Line 4: Audio Right    |
+--------------------------+--------------------------+--------------------------+


.. Important::
    It's crucial that the M-POD for EGI is set to use Negative logic. See this
    `blog post <https://cedrus.com/blog/update-for-egi-users.htm>`_.


Configuring the Eyetracker to accept Stimtracker events
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
By default, the Eyelink will not write Stimtracker events to the EDF file. To enable
this, you must add extra lines of code to the ``FINAL.ini`` file on eyelink file
browser partition of the Host PC. This file is located at ``/ELCL/EXE/FINAL.ini``.
Please see this `post <https://www.sr-research.com/support/thread-316.html?highlight=bidirectional>`_
and follow the instructions to add accept DATA Register events to the EDF file, which should specify
to add the following block of code to the end of the aforementioned ``FINAL.ini`` file::


    write_ioport 0xA 0x20
    input_data_ports  = 8
    input_data_masks = 0xFF
    create_button 1 8 0x01 0 
    create_button 2 8 0x02 0
    create_button 3 8 0x04 0 
    create_button 4 8 0x08 0
    create_button 5 8 0x10 0
    create_button 6 8 0x20 0
    create_button 7 8 0x40 0
    create_button 8 8 0x80 0


