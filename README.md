# TABFIX

A command-line tool to fix tab spaces in a file.

### Convert

It takes a file name as an argument and converts regular spaces into tab spaces in that file. It does not modify the original file. Instead, it creates a new file with the `.tabfixed.` prefix added to the file name.

### Watch

It can also watch the file and fix tabs on every save. In this mode, a backup file is created with the `.tabbackup.` prefix to preserve the data, just in case.

```
Usage:
        tabfix [options] <file_name>
OR      tabfix [options] <file_name> <tab_length>

Options:
  -w, --watch       Watch the file and fix tabs on save.
  -h, --help        Show this help menu.

(default tab length is 4)
```
