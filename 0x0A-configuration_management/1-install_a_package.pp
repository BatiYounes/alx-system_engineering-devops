# Puppet manifest to install Flask from pip3

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command     => '/usr/bin/pip3 install flask==2.1.0',
  path        => '/usr/local/bin:/usr/bin:/bin',
  unless      => '/usr/bin/env python3 -c "import flask; print(flask.__version__)" | grep -q "2.1.0"',
  require     => Package['python3-pip'],
  environment => ['PATH=/usr/local/bin:/usr/bin:/bin'],
}
