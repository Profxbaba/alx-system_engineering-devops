# Puppet manifest to fix Apache returning a 500 error using strace

# Install strace package
package { 'strace':
  ensure => installed,
}

# Run strace on Apache process to find the issue
exec { 'run_strace_on_apache':
  command     => 'strace -o /tmp/strace_output.txt -p $(pgrep apache2)',
  path        => '/bin:/usr/bin',
  refreshonly => true,
  subscribe   => Service['apache2'],
  notify      => Service['apache2'],
}

# Fix the issue found by strace
file_line { 'increase_max_connections':
  path    => '/etc/apache2/apache2.conf',
  line    => 'MaxConnectionsPerChild 100',
  match   => '^MaxConnectionsPerChild',
  notify  => Service['apache2'],
  require => Exec['run_strace_on_apache'],
}

# Ensure Apache service is running
service { 'apache2':
  ensure => running,
}
