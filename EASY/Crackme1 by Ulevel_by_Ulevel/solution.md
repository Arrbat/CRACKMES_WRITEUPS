Simple crackme, where there is need to find password
---

There is an bool condition in main function, and if it is true, then access is granted
```c
  if (bVar1) {
    uVar4 = 0x26;
    pcVar3 = "The password is valid, access granted.";
    std::__ostream_insert<>((ostream *)&_ZSt4cout,"The password is valid, access granted.",0x26) ;
  }
```

bVar is defined as 
```c
bVar1 = IsPassValid((longlong *)&local_48);
```

I provided the function below. `Param1` is the input of user.
```c
/* IsPassValid(std::string) */

bool IsPassValid(longlong *param_1)

{
  bool bVar1;
  
  if (param_1[1] != 0xb) {
    return false;
  }
  if ((*(longlong *)*param_1 == 0x69206b6f6369614e) && (*(int *)(*param_1 + 7) == 0x6a697269)) {
    bVar1 = false;
  }
  else {
    bVar1 = true;
  }
  return !bVar1;
}
```


Two conditions must be true, and it may be represented into hexademical format where:

> NOTE: in little-endian memory will hold these bytes in reverse order, so we get:

```c
0x4E → 'N'
0x61 → 'a'
0x69 → 'i'
0x63 → 'c'
0x6F → 'o'
0x6B → 'k'
0x20 → ' ' (space)
0x69 → 'i'
```
>NOTE: param_1+7 means that we start at byte 7 of value (reading the memory where 7th byte is stored):
```c
0x69 → 'i'
0x72 → 'r'
0x69 → 'i'
0x6A → 'j'
```


![image](https://github.com/user-attachments/assets/f3c73bb6-a129-491f-be68-de085444d8b6)



# So the password is `Naicok irij`