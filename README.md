Notelink CLI
=================================
Management your favorite link using CLI.

(_still on progress_)

## Install
```commandline
pip install notelink
```

## How To Use
### save
```commandline
notelink nsave
notelink nsave https://medium.com/python
notelink nsave https://medium.com/flask \
    https://medium.com/django
```


### list
```commandline
notelink nlist
notelink nlist --list-host
notelink nlist --hostname stackoverflow.com --reverse
```


### search
```commandline
notelink nsearch "python"
notelink nsearch "django" --limit 3
notelink nsearch "django" --limit 3 \
    --hostname medium.com
```



## Contributors

Want to become contributor guys? just PR okay :)


## Authors
<table>
  <tr>
    <td align="center">
      <a href="https://agung96tm.com/">
        <img src="https://avatars.githubusercontent.com/u/1901484?v=4" width="100px;" alt=""/><br />
        <b>Agung Yuliyanto</b><br>
      </a>
      <div>💻</div>
    </td>
  </tr>
</table>

