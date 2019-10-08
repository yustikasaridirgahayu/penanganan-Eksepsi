def main():
	try:
		f = open("data.txt,", "w")

		try:
			f.write("pemrograman python")
		finally:
			f.close()
	except IOError:
		print("\nERROR: file tidak dapat " + "dibuka/ditulis")

if __name__ == "__main__":
	main()
