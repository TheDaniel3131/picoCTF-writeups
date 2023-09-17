import hashlib
import base64

hash = hashlib.sha256(b"PRITCHARD").hexdigest()
hash_pos = [4,5,3,6,2,7,1,8]

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = ""
key_part_static2_trial = "}"

for i in hash_pos:
    key_part_dynamic1_trial += hash[i]

key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
print(key_full_template_trial)