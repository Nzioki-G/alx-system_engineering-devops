# create a manifest that kills a process 'killmenow'

exec { 'kill process':
    provider => 'shell',
    command  => 'pkill killmenow'
}
