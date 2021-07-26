plainText = input("Enter  Word Multiple of 7  ")
# Any 14 char Word eg ATTACKON1200AM
keywords= input("keyword  ")
Keywords=keywords
# Make ADFGVX Matrix
seentext = []
ADVGVX_MATRIX = []

def makeADFGVXMatrix ():
  # Assuming Keyword doesnt have repetitions
    global ADVGVX_MATRIX,seentext,keywords
    for i in range(0,6):
      newArr=[]
      startAscii = 65
      for j in range(0,6):
        while (keywords!="" and keywords[0] in seentext) :
            keywords=keywords[1:]
            
        if keywords != "" :
          newArr.append(keywords[0])
          seentext.append(keywords[0])
          keywords=keywords[1:]

        else :
          if startAscii > 90 :
            startAscii=48
         
          while (chr(startAscii) in seentext) :
            startAscii+=1
            if startAscii > 90 :
              startAscii=48
          newArr.append(chr(startAscii))
          seentext.append(chr(startAscii))
          startAscii+=1
      ADVGVX_MATRIX.append(newArr)

makeADFGVXMatrix()

positions=["A","D","F","G","V","X"]
cipher_text=""
def search (mat,char):
  global cipher_text,positions
  for i in range(0,6):
    for j in range(0,6):
      if char==mat[i][j]:

        cipher_text+=positions[i]
        cipher_text+=positions[j]

def getcipherText (plainText,mat):
  global cipher_text,positions
  for i in plainText :
    search(mat,i)

getcipherText(plainText,ADVGVX_MATRIX)  
privacy=["P","R","I","V","A","C","Y"]

PrivacyMatrix = [["P","R","I","V","A","C","Y"]]

key_sort =privacy
indices=[]
key_sort.sort()
for i in PrivacyMatrix[0]:
  indices.append(str(key_sort.index(i)+1))
PrivacyMatrix.append(indices)
# print(PrivacyMatrix)

def makePrivacyMatrix(cipher_text):
  global PrivacyMatrix
  temp=[]
  for i in range(0,len(cipher_text)):
    
    temp.append(cipher_text[i])
    if len(temp)==7:
      PrivacyMatrix.append(temp)
      temp=[]
makePrivacyMatrix(cipher_text)
currentCol=1
def selectCol (mat) :
  global currentCol
  for i in range(0,len(mat)) :
    if currentCol==int(mat[i]) :
      currentCol+=1
      return int(i)


FinalText = ""

def readPrivacyMatrix(mat):
  global FinalText
  n=len(mat)
  m=len(mat[0])
  # print(n,m)
  for i in range(0,m):
    whichCol=selectCol(mat[1])
    for j in range(2,n):
      FinalText=FinalText+mat[j][whichCol]

def printMatrix(mat) :
  for i in mat :
    print(i)
    # for j in mat[i]:
    #   print(i,end=" ")
    # print("")  

readPrivacyMatrix(PrivacyMatrix)
print("PlainText --  ",plainText)
print("KeyWord   --  ",Keywords)
print("\n\n\n\nADFGVX Matrix \n")
printMatrix(ADVGVX_MATRIX)

print("ADFGVX Cipher Text -\n",cipher_text)

print("\n\nPrivacy Matrix \n")
printMatrix(PrivacyMatrix)
print("Final Encryted Text - \n",FinalText)




def decryption (ADFGVX_MATRIX,text,keyword):
  indexing = ['A','D','F','G','V','X']
  # P R I V A C Y 
  keyword_list =[]
  for i in keyword :
    keyword_list.append(i)
  newKeyword=keyword_list.copy()
  newKeyword.sort()
  ordered_text = ""
  temp_mat = []
  for i in keyword_list :
    position = newKeyword.index(i) 
    length=(len(text)//len(keyword_list))
    tempStr = text[position*length:position*length+length]
    temp_mat.append(tempStr)
  for i in range(0,len(temp_mat[0])) :
    for j in range(0,len(temp_mat)):
      ordered_text=ordered_text+temp_mat[j][i]
  print("\n\nOrdered Text",ordered_text)
  correctText=""
  for i in range (0,len(ordered_text)//2) :
    row_char=ordered_text[i*2]
    col_char=ordered_text[i*2+1]


    row = indexing.index(row_char)
    col = indexing.index(col_char)

    correctText = correctText + ADFGVX_MATRIX[row][col]
  print("\n\ncorrectText",correctText)
decryption(ADVGVX_MATRIX,FinalText,"PRIVACY")