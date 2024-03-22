# Puppet manifest to kill a process named killmenow

exec { 'killmenow':
  command     => '/usr/bin/pkill -f killmenow',
  path        => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  refreshonly => true,
}
