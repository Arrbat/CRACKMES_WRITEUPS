# Crypt0 - Beginner CrackMe_by_Crypt0 C/C++ Windows x86
Very easy crackme. 

I have run the app, and saw that it requires username (and then password):

![image](https://github.com/user-attachments/assets/17f130ac-c3f5-43d0-88ca-e7b54179bf8b)
![image](https://github.com/user-attachments/assets/6f67facd-3849-4744-b04e-cd13ac685cf0)

`if username is not valid, then there is error and program closes`

I thought it must be harder, so i loaded it into ghidra, tryed to find some intresting strings and there was `Good Job bro! Keep going :)`.
I found where it is used and then saw how there were located right username and password, just in the start of this (main) func.
Inputed values, and got following:
![Screenshot 2025-03-14 183531](https://github.com/user-attachments/assets/a2d0a68e-97a2-494e-b007-eac14e8eb6bd)





Of course there is more elegant solution just by using `strings CrackMe.exe` command, after that we found both username and password

![image](https://github.com/user-attachments/assets/95aaa914-f88b-4f54-bf6d-c1fba5ef3d21)
