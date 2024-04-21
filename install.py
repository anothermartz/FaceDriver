version = 'v0.0.1'
# write a file to signify setup is done
with open("installed.txt", "w") as f:
    f.write(version)
print("Installation complete!")
