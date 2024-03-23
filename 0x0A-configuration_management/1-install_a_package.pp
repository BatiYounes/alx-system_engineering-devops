#!/usr/bin/pup

# Install required dependencies
package { 'python3-pip':
  ensure => installed,
}

exec { 'install_werkzeug':
  command => '/usr/bin/pip3 install werkzeug==2.0.1',
  unless  => '/usr/bin/pip3 show werkzeug | grep -q "Version: 2.0.1"',
}

# Install Flask 2.1.0
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Exec['install_werkzeug'],
}
