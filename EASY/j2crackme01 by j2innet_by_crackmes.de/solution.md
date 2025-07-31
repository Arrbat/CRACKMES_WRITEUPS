https://crackmes.one/crackme/5ab77f6333c5d40ad448ca8c

Tool: Ghidra
Second func in entry() is like basic app initialization. And here is the func main in the end.  (I renamed values and funcs)
```c
returncodeMAIN = main();
```

Here in main there is a lot of code, but the most interesting part is where string ` C:\\userid:` located . 
So here it is printed and by using `gets()` waits for user\`s input. 

```c
  print?((int *)cout_exref,"C:\\userid:");
  gets(useridINPUT);
```

In ahead there is the same, but with password
```c
  print?((int *)cout_exref,"C:\\passid:");
  gets((char *)passINPUT);
```

And also you may find in the end validation code, you may be sure it is validation because of its strings:

```c
validation:
  if (iVar6 == 0) {
    useridINPUT2 = "ok. welldone.\n";
  }
  else {
    useridINPUT2 = "ops. try harder.\n";
  }
  print?((int *)cout_exref,useridINPUT2);
  gets(useridINPUT);
```


So let\`s see what the code does with inputed userid
```c
if (useridINPUT2 + -6 < (char *)0x4)
```
it just checks if our input is less than 4 or is above 6. But yeah, this statement looks strange little bit.

And if it is between 4 and 6 then it executes code ahead, but if not - the correct password will consist of these chars:
```c
  else {
    invalidi-inputSTRING[0] = 'i';
    invalidi-inputSTRING[1] = 'n';
    invalidi-inputSTRING[2] = 'v';
    invalidi-inputSTRING[3] = 'a';
    invalidi-inputSTRING[4] = 'l';
    invalidi-inputSTRING[5] = 'i';
    invalidi-inputSTRING[6] = 'd';
    invalidi-inputSTRING[7] = ' ';
    invalidi-inputSTRING[8] = 'i';
    invalidi-inputSTRING[9] = 'n';
    invalidi-inputSTRING[10] = 'p';
    invalidi-inputSTRING[0xb] = 'u';
    uStack_108 = 0x74;
  }
```
the last char equals to `t`

Here code check if password equals to string above:
```c
LAB_00401ff4:
      iVar6 = (1 - (uint)bVar7) - (uint)(bVar7 != 0);
      goto validation;
    }
    if (bVar2 == 0) break;
    bVar2 = pbVar5[1];
    bVar7 = bVar2 < passINPUT2[1];
    if (bVar2 != passINPUT2[1]) goto LAB_00401ff4;
    pbVar5 = pbVar5 + 2;
    passINPUT2 = passINPUT2 + 2;
  } while (bVar2 != 0);
  iVar6 = 0;
```

Ivar is used for validation, if it =0 then we got congratulations message.


But what if our userid is between 4 and 6 (length)?
In that case, the program proceeds to more complex logic (involving threads and calls to functions like FUN_00401740()), which likely computes or validates the correct password dynamically. That part is less clear here, but essentially the password is the same: "invalid input" (without quotes, with space).


## So solution: userid is not matter, password always equals to "invalid input"
