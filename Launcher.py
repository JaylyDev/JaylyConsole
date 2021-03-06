# Developer: JaylyDev
# Connection:
# YouTube: https://youtube.com/jaylymc
# Twitter: https://twitter.com/Jayly_
# Discord: Jayly#1397
# GitHub: https://github.com/JaylyDev/JaylyConsole

# License management
jclicense_14 = """
MIT License

Copyright (c) 2021 JaylyDev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
license_file = open("LICENSE", "r")
if license_file == jclicense_14:
  print("Correct content for license file, checking two-factor authentication (2FA).")
  import OS.Registery.2fa
else:
  print("JaylyConsole detects either the content of license is incorrect compared to the original's.")
  exitregistery = input("Please press \"Enter\" to shut down the console.")
