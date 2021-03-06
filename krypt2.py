import string
import collections
import sets, sys

# 11 unknown ciphertexts (in hex format), all encrpyted with the same key
c1 = "6fd84be308bc1a0377765d1aa4645fc178a504f99baf82b7a208dffcc35d7c3d5d063e1a064c743191e99dae4e7535c5f571e380a2d3eeb9861d6b21a7c5ddda2e81af9744b2600fbdcffa9cbb324cea1c99e644e6cd1e25aee87a1183e221630c855da0f5802710f1a61b2dc5480fcc9dbfc2ee6cb7190c4f69b565f7bca7426f6ecc69af241b2598dd3cd3aa9f0f4849"
c2 = "77d55eb745ad520e67764d14be7e49c965e014ba9bab90e2a45198e6df19283d02423d024c53122daddabceb226305fbdc1380bcedeea1bd9e4b5d60a3cacd9f4892ee8a4eb6634ff898f195a07b4eaf44d1fe45f4885522b2bf321a9ef3202b2a815d86f5d32514f7a70d64c55e47ce91f18ca651ad540d492ce67fb8fce85a653a9f6eea7b5e30829eaf9744b2600fbdcffa9cbb324cea1c99e644e6cd1e25aee87a1183e221630c855da0f5802710f1a61b2dc5480fcc9dbfc2ee6cb7190c4f69b565f7bca7426f6ecc69af241b2598dd3cd3aa9f0f4849"
c3 = "74d55aad45b04e417a394f09a32d49d574e009a19ba494b0a558ddfdd8177c00404b39144e53231688f7ceb2015770caf630a6d9b9c9eea8881e7c21acc5cdd76b92a89712ff6706ff83f5d4a0340feb4ed7f14ee1c1553fa9f62e1789e42f2b31bd3091d5"
c4 = "6ac91faa16f94e0e7d765c1aa365008765af0ff5cea890f4a041cbf6c8157c2640497c081717301a8aa0ce9f014d70c5f036a6d9b9ceabf18b026969becad0d169ccaf9345b6730bf88bf680bc7b4cea46cafa0be7825529a4bf1f0d89b66e6506d21eb5f4803719e7e94f01910943c89bb98cab50ab5a4e001be26efde4ab0c67758365ea71523698c6689496d70e521a0019074f7109aec4430f22ae34460623bfbb94dcf6a4e50ddb2b958c15018f0006d29b758dba9184d9"
c5 = "70c84ca20bf95b0f76765d13b52001e07ea440a7deb585b0b744d4b3ef512e3b5c52351a0c53271091f79dea430f70fefc2fa6d9a2c0eeb0894b6f66af9e99c86b8ce3c80d8c6510b981b99da77b58e653d1bf6cfc894e6b92f73f5f9bf7722b179d12f4fdcf2b1cbeaf073ac5444a9bdcb38dba12f8151a0001b578f9f9e30020558221867e563c91c164d1b4da47404e42020a08761baedb44182bee34571766ecac9c91f5b9b70c8f3c99924b"
c6 = "6ace1fb70ab61a0c6735465bb6625e8770e013b6d4b494bcf67fd0f6c21935260f4e331a1000741a96fecea21a0232ccb92eb39ca3d2e0f1b5046364a58899c8678ce3c454b06543bb80f491f42f40af5ed6ea59b38b143fa9fa28589fa9217c06d511b8bad42b58faa00626805b038188b991ba56bd0647"
c7 = "6dd24be311ab4f0d6b764715f07944c278b240bddea783e4a50498f1d94d7c3b41062813071a265f81e28bb840021accea28e3b4acd4a7b0cb4b7969abd099de2e84ea8541ff7f05f88deb9dba3e0fc746cdf70be48c0623e6fb7a0b84ef2178029e11bbed802710fbac033bc54f40d3dc8397bd5fb41d074569b543f7e7a74175798421b97e5725d0c528c0a7cd475552100314013e0ef9c955592eec34531e70b8abd5"
c8 = "7ad24ae304ab5f4165334218bf60498b31a705bbcfaa94fdb34699b3cf5631370306310e111a371685f59de74e523cc8e073e3b8edceafbd8b472e60eaccd8d362c1af8344a97543aa80f699f57b4ee14399f944fc995522b5b37a1885e46d784dd230a1e9c92758eea5093196050fc092b5d8ba56bd0d494429fb68fdb0"
c9 = "74d550e30bb64e097b38495bb8785ed331b709a1d3a79db0be41cbe08b5d7c3a464b7c120c53271c8be980f14e7538c0f538e38ea886b9b4950e2e68a4d0dccd6d88ee8a4ab67e04f89bf186a1285bfc07d8f14fb38f1924b6ec765faff76c6e439f12a6ff802516fae90527974c0fc092b5d8a851ad13015468fa65b8e0e65e743a8d6fae3f4b3082c6659496d60b4d1a1604064f6e1de7c64f1c67e175491a2fecb991deb3a6a30c8f3c98dc150692060480d97789a991c2"
c10 = "74d453b745ad520e67764014a4210ced64ac05ea9ce690feb20498f1d519312b0f4e33170b17351281b7ce9f064770d9eb38b78db486b9a3821f6d69eac8dcd97ac0ec9654b67e04f88ef790f4284ee64399b86aeac3526b95f07a0c89f32d2b0d9d0af8bac82b0fbea84822805a5b818fb999a252f817064d2db56afafff258213aa521bd7e492391dc3d98e2de090173421f0b006b03ea88401031e734455f77a4a18cc2f2b8a65e823c9d8e0343"
c11 = "66d34ba617f978245c00613799420cc67fa44098fe94b2c58261f7b3e17c0e117a72153442243c1a96fecebf064770cdfc2baa95edd5a6be92076a21beccd0cc2eb2e08948b03001bdd0b9b7b5364aaf4fdcbf45fc995523aef23f5f98f92c650a9515a0a5"
c12 = "64d250a745b15f006022025bb163488b31a947f5dda798e4be0498da8c4e353e4306281e0e1f741781e9ceaa1d023ddcfa35f9d981c9bcb5cb4b426eb8c0959f7d88eac45ab67c0ff88dfcd4b57b45e05edfea47b39a1a26a0f1745fbed94c4e2cd22abcfbd4640ff7a51c68914140d4dca59da252f81c0c5264b565ede2f4493f3a9869a56a1b359fc13d94acd0130157031e084f730aa0"
c13 = "77d55ae315ab5f027b395b08f0795ec270b315a7dee69ef6f640d1e08c5c25375c4f3b131653381097efd4eb3d4a3fdeb930a6d9ac86a3b8941f7c64b9d799cb6681fbc444ac3013b99cea9dba3c0fe946d0ed07b3ba1d2ab5bf3e1098fe216306805db6ffc1310ce7e91b2d975f4a8ddcb38dba1eb907494168fb64ecf5a77b687f9e64ea561b3c91cb69c6a7de03014d0a03431f7f1cfd8f485933ea75505f73adbd8ad8fdb1e2189a308ec3"
c14 = "77d556b045a94804713f410ea32d4ec87eab40badde69dffa04d94b3d85135210f5332190d063a1bc4f781bd0b507c89cd32e39ba8c7bba58e0d7721a2cdd4932e8fe18854ff7c02bb84ead4b57b4ce051dced11b3b91d2ee1f9330c84b66d6215970ef4f3ce640cf6ac483b804803819dbf9cee19ac1d1a0025e068f0b0f75e697e89218c70497196d320c6e2c80e55520d19174f6a07eb884a182ef034531677a4a79791e7b9e216923d99c6"
c15 = "6bd248e316b0561777240308a76849d331b30fa0d5a2d1fcb95edde1df1e7c2640483b0e0700741d9dbb80a2094a2485b911aa92a886bdbe811f6b72be84d4ca7d89ecc459b03002ac9bfc9ab03241e807dcfe59e0cc550194d3133ab8b653640e9712f5"
c16 = "74d556a00df51a006176461ef06f5ec270b408b0dfe695f5b041d9fdcf5c7c26400631024216350d97b7ce830b0223deec33a4d9acc4a1a4934b6668b984d1da6f84af8543bb3000ad9bb980bc3e0ff84ed7fb58bfcd2223aebf341098fe686504d215a1e8d4640ff7bd0029890947c88fa2dfaa1eb01d040021fb2bebf3e85e6e20cc56a2765734d0c52c94b5da15441a0b02170a6c0ce6c9421e2eec73040b6bbebb8ac5e0f6a3109f799e901f189542"
c17 = "61f871952a95732e3202461ebe2d5fcf74e008b4cfaed1e3a147cafd8c4d34335b062f130753231688f7ceb81a4b3cc5b931aa8fa886adb986187a64f584ebf043a5c0c47eb77543b08eed9cf87b4ee14399f645b3991d2ab5bf290f8de4686504d210b5f1c53758f6bc0f2dc55e4ed288b4d4"
c18 = "6cd35ae303b8531377240e0fb86c42877cb940b9d4b094b1f65cd0f68c58303e0255391e0b1d335f97ee80eb204777cceb7db098ba86a6b4954b6360bec7d19f7d89e18748ff760aaa9cedd4a0334aaf50d6ed47f7cd172ea6ea3451ccd4444535bd319dd580100deae548318a5c0fd29da6d8a65baa540f4121e727b8fee842653a896db97a1b3395db27d3e2dd1e0d"
c19 = "6a9d52a604b71641613f5c57f064428775a50cb4c2e6a6f5f65fd9e0d85c7c3d5a547c170b143c0b97bb87a54e5431c0f771e395a4cdabf18b0a6371b984dbc62e84ee9d03ff4402b38ab99ba1290fe848d6fb0bfe881425a8f13d53ccf06e79439d08a6baca311cf9a40d2691095cc888a2d88857ae11495421f86eebb0ee42206e8460be3f5e23959226daa1da4748544203161d3e09e7de495930eb605751"
c20 = "74d44bab45b455137776411df07944ce7fa55af5cfae98e3f644d7e5c919283a4e527c0f0a1c215f8cfa9dbf4e5138c6ee33e3bda2d2a6f1860f6a21a7cbcbda2e87fd8d48b93017b7cfed9bbb7b42fa44d1bf44f5cd1822affa7a109bf82f2b2f9d0bb1bac93758ffe91b258a424a818eb091bd5bbc541e493cfd2becf8e20c666f8164ea705d7183db2edcb18447635f0b02044f6e1afccf491d6ba27504196abeabd9c2e3b7b0159730929b5006884e0d9d8f629aa8c2cc906adf53cd"
ciphers = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20]
# The target ciphertext we want to crack
target_cipher = "74d44bab45b455137776411df07944ce7fa55af5cfae98e3f644d7e5c919283a4e527c0f0a1c215f8cfa9dbf4e5138c6ee33e3bda2d2a6f1860f6a21a7cbcbda2e87fd8d48b93017b7cfed9bbb7b42fa44d1bf44f5cd1822affa7a109bf82f2b2f9d0bb1bac93758ffe91b258a424a818eb091bd5bbc541e493cfd2becf8e20c666f8164ea705d7183db2edcb18447635f0b02044f6e1afccf491d6ba27504196abeabd9c2e3b7b0159730929b5006884e0d9d8f629aa8c2cc906adf53cd"


# XORs two string
def strxor(a, b):  # xor two strings (trims the longer input)
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])


# To store the final key
final_key = [None] * 1500
# To store the positions we know are broken
known_key_positions = set()

# For each ciphertext
for current_index, ciphertext in enumerate(ciphers):
    counter = collections.Counter()
    # for each other ciphertext
    for index, ciphertext2 in enumerate(ciphers):
        if current_index != index:  # don't xor a ciphertext with itself
            for indexOfChar, char in enumerate(
                    strxor(ciphertext.decode('hex'), ciphertext2.decode('hex'))):  # Xor the two ciphertexts
                # If a character in the xored result is a alphanumeric character, it means there was probably a space character in one of the plaintexts (we don't know which one)
                if char in string.printable and char.isalpha(): counter[
                    indexOfChar] += 1  # Increment the counter at this index
    knownSpaceIndexes = []

    # Loop through all positions where a space character was possible in the current_index cipher
    for ind, val in counter.items():
        # If a space was found at least 7 times at this index out of the 9 possible XORS, then the space character was likely from the current_index cipher!
        if val >= 7: knownSpaceIndexes.append(ind)
    # print knownSpaceIndexes # Shows all the positions where we now know the key!

    # Now Xor the current_index with spaces, and at the knownSpaceIndexes positions we get the key back!
    xor_with_spaces = strxor(ciphertext.decode('hex'), ' ' * 1500)
    for index in knownSpaceIndexes:
        # Store the key's value at the correct position
        final_key[index] = xor_with_spaces[index].encode('hex')
        # Record that we known the key at this position
        known_key_positions.add(index)

# Construct a hex key from the currently known key, adding in '00' hex chars where we do not know (to make a complete hex string)
final_key_hex = ''.join([val if val is not None else '00' for val in final_key])
# Xor the currently known key with the target cipher
output = strxor(target_cipher.decode('hex'), final_key_hex.decode('hex'))

print
"Fix this sentence:"
print
''.join([char if index in known_key_positions else '*' for index, char in enumerate(output)]) + "\n"

# WAIT.. MANUAL STEP HERE 
# This output are printing a * if that character is not known yet
# fix the missing characters like this: "Let*M**k*ow if *o{*a" = "cure, Let Me know if you a"
# if is too hard, change the target_cipher to another one and try again
# and we have our key to fix the entire text!

# sys.exit(0) #comment and continue if u got a good key

target_plaintext = "With more of thine: this love that thou hast shown Doth add more grief to too much of mine own. Love is a smoke raised with the fume of sighs; Being purged, a fire sparkling in lovers' eyes"
print
"Fixed:"
print
target_plaintext + "\n"

key = strxor(target_cipher.decode('hex'), target_plaintext).encode("hex")

print
"Decrypted msg:"
for cipher in ciphers:
    print
    strxor(cipher.decode('hex'), key.decode("hex"))

print
"\nPrivate key recovered: " + key + "\n"

'''
Which thou wilt propagate, to have it pressed
With more of thine. This love that thou hast shown
Doth add more grief to too much of mine own.
Love is a smoke raised with the fume of sighs
Being purged, a fire sparkling in lovers' eyes;
Being vexed, a sea nourished with loving tears.
What is it else? A madness most discreet,
A choking gall, and a preserving sweet.
Farewell, my coz.
'''
