import random


# Συνάρτηση για την δημιουργία τυχαίας δυαδικής συμβολοσειράς D
def createD(k):
  d = ""
  for i in range(k):
    d = d + str(random.randint(0, 1))
  return d


# Συνάρτηση που υλοποιεί την πράξη xor μεταξύ δύο αριθμών
def xor(a, b):
    R = []
    for i in range(len(b)):
      if a[i] == b[i]:
        R.append('0')
      else:
        R.append('1')
    return ''.join(R)


# Συνάρτηση που εκτελεί τη διαίρεση του modulo 2 και υπολογίζει το υπόλοιπο F των δυαδικών αριθμών D και P
def division(D, P):
    bits = len(P)
    temp = D[0: bits]
    while bits < len(D):
      if temp[0] == '1':
          temp = xor(P, temp) + D[bits]
      else:
          temp = xor('0' * bits, temp) + D[bits]
      bits = bits + 1
    if temp[0] == '1':
        temp = xor(D, temp)
    else:
      temp = xor('0' * bits, temp)
    F = temp
    return F


# Συνάρτηση που χρησιμοποιείται για την πρόσθεση του υπολοίπου F στα δεδομένα και τη δημιουργία T
def createT(D, P):
    appended_data = D + '0' * (len(P) - 1)
    F = division(appended_data, P)
    T = D + F
    return T


msg = int(input("Δώσε αριθμό μηνυμάτων: "))
k = int(input("Δώσε μέγεθος κάθε μηνύματος: "))
P = (input("Δώσε P: "))
BER = float(input("Δώσε BER: "))
n = len(P) + k - 1

error = 0
disapproval = 0
approval = 0

for i in range(1, msg):
    D = createD(k)
    T = createT(D, P)
    array = []  # μετατροπή string σε list
    array[:0] = T
    arrayT = array

  for j in range(0, len(arrayT)):
    if random.uniform(0, 1) < BER:
      if arrayT[j] == "1":
        arrayT[j] = "0"
      else:
        arrayT[j] = "1"

  stringT = ""  # μετατροπή list σε string
  for element in arrayT:
      stringT += element

  if T != stringT:
      error += 1

  if int(division(stringT, P)) != 0:
      disapproval += 1
  else:
      if T != stringT:
          approval += 1

print("Αριθμός μηνυμάτων = ", msg)
print("Σφάλματα αποδέκτη = " + str(error))
print("Απόρριψη σφαλμάτων CRC = " + str(disapproval))
print("Έγκριση σφαλμάτων CRC = " + str(approval))
print("% μηνυμάτων με σφάλματα = " + str((error / msg) * 100) + "%")
print("% μηνυμάτων CRC που απορρίφθηκαν = " + str((disapproval / msg) * 100) + "% ")
print("% μηνυμάτων που ενέκρινε το CRC με σφάλματα = " + str((approval / msg) * 100) + "%")