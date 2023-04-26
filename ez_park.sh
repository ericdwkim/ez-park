#! /bin/bash

python $HOME/workspace/personal/ez-park/app.py

# Set the default license plate value
export LICENSE_PLATE=GUEST_A

# Override the license plate value for guest B
export LICENSE_PLATE_GUEST_B=ABC123

# Override the license plate value for guest A
export LICENSE_PLATE_GUEST_A=XYZ789

# Check if a specific guest's license plate is set and use it if it exists, otherwise use the default
if [[ $GUEST_NAME == "guestA" ]] && [[ ! -z $LICENSE_PLATE_GUEST_A ]]; then
  export LICENSE_PLATE=$LICENSE_PLATE_GUEST_A
elif [[ $GUEST_NAME == "guestB" ]] && [[ ! -z $LICENSE_PLATE_GUEST_B ]]; then
  export LICENSE_PLATE=$LICENSE_PLATE_GUEST_B
fi

# Create a new license plate environment variable for guest Z
export LICENSE_PLATE_GUEST_Z=DEF456
