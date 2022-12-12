def solution(inputString):
    return caesar(inputString, 1)


def caesar(story, shift):
  return ''.join([  # concentrate list to string
      # if original char is upper case than convert result to upper case too
      (lambda c, is_upper: c.upper() if is_upper else c)
      (
          # rotate char, this is extra easy since Python accepts list indexs below 0
          ("abcdefghijklmnopqrstuvwxyz" * \
           2)[ord(char.lower()) - ord('a') + shift % 26],
          char.isupper()
      )
      if char.isalpha() else char  # if not in alphabet then don't change it
      for char in story
  ])


'''

def solution(inputString):
    return ''.join((chr(ord(i)+1) if i!="z" else "a" for i in inputString))
    
'''
