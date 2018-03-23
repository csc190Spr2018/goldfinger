def key1():
	return 123;

def key2():
	return 231;

def key3():
	return 331;

def master_key():
	return key1() * key2() * key3();

print("Master key is: ", master_key);
