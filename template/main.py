form els import els
els.check_platform("True")
path = ['./a.txt', './b.txt', './c.txt']
for pathcount in path:
    els.check_file_dir(pathcount, "True", "True")
els.check_ping("google.com", "2", "True", "True")
els.private_ip("8.8.8.8", 80, "True")
els.global_ip("True", "True")
