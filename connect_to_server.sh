#!/usr/bin/expect -f

# Set variables
set timeout -1
set password "Tigers9498"
set user "crm058"
set host "hpc-portal2.hpc.uark.edu"

# Start the SSH session
spawn ssh $user@$host

# Look for the password prompt
expect "$user@$host's password:"

# Respond to the prompt with the password and an implicit Enter (\r)
send -- "$password\r"

# Interact with the session after logging in
interact
