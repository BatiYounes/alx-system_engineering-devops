#!/usr/bin/puppet

# Puppet manifest to install a specific version of Flask (2.1.0)

class { 'flask_install':
  version => '2.1.0',
}

class flask_install (
  String $version,
) {
  package { 'python3-pip':
    ensure => installed,
  }

  exec { "install_flask_${version}":
    command     => "/usr/bin/pip3 install --upgrade flask==${version}",
    unless      => "/usr/bin/pip3 show flask | grep -q \"Version: ${version}\"",
    require     => Package['python3-pip'],
    environment => ['PATH=/usr/local/bin:/usr/bin:/bin'],
  }
}
