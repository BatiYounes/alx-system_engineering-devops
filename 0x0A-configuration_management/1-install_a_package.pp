# 1-install_a_package.pp
exec { 'install_pip3':
  command => '/usr/bin/apt-get update && /usr/bin/apt-get install -y python3-pip',
  path    => ['/usr/bin', '/usr/sbin'],
  unless  => '/usr/bin/which pip3',
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Exec['install_pip3'],
}

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Exec['install_pip3'],
}
