from pescription_data import *

trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

# Remove warfarin and add Edoxaban
for patient in trial_patients:
    prescription = patients[patient]
    # if warfarin in prescription:
    try:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    # else:
    except KeyError:
        print(f"Patient {patient} is not taking Warfarin."
              f"Please remove {patient} from the trial.")

    print(patient, prescription)