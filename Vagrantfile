# -*- mode: ruby -*-
# vi: set ft=ruby :

$vm_memory = 1024

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  # Make exam simplify
  config.vm.box_check_update = false

  config.vm.provider :virtualbox do |v|
    v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    v.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
    v.memory = $vm_memory
  end

end
