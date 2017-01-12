boot_policy{'policy':
	confuse => 'testing123',
	descr => 'type  description',
	reboot_on_update => 'no',
	policy_owner => 'local',
	enforce_vnic_name => 'yes',
	boot_mode => 'uefi',
	state => 'present',	
        ip => 'IP Address of UCSPE server',
        username => 'username',
        password => 'password',
}
