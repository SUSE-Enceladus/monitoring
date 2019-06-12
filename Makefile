dirEmptyVer =  $(shell rpm -q --specfile --qf '%{VERSION}' monitoring-plugins-dir-empty.spec)
procHangVer = $(shell rpm -q --specfile --qf '%{VERSION}' monitoring-plugins-proc-timed-hang.spec)
repCheckVer = $(shell rpm -q --specfile --qf '%{VERSION}' monitoring-plugins-rmt-repos.spec)
repoSigVer = $(shell rpm -q --specfile --qf '%{VERSION}' monitoring-plugins-repo-signatures.spec)
oldFilesVer = $(shell rpm -q --specfile --qf '%{VERSION}' monitoring-plugins-old-files.spec)

check:
	@flake8 check_dir_empty check_proc_timed_hang

tar-dir-empty:
	mkdir "check_dir_empty_$(dirEmptyVer)"
	cp check_dir_empty LICENSE "check_dir_empty_$(dirEmptyVer)"
	tar -cjf "check_dir_empty_$(dirEmptyVer).tar.bz2" "check_dir_empty_$(dirEmptyVer)"
	rm -rf "check_dir_empty_$(dirEmptyVer)"

tar-proc-hang:
	mkdir "check_proc_timed_hang_$(procHangVer)"
	cp check_proc_timed_hang LICENSE "check_proc_timed_hang_$(procHangVer)"
	tar -cjf "check_proc_timed_hang_$(procHangVer).tar.bz2" "check_proc_timed_hang_$(procHangVer)"
	rm -rf "check_proc_timed_hang_$(procHangVer)"

tar-repo-check:
	mkdir "check_rmt_repos_$(repCheckVer)"
	cp check_rmt_repos LICENSE "check_rmt_repos_$(repCheckVer)"
	tar -cjf "check_rmt_repos_$(repCheckVer).tar.bz2" "check_rmt_repos_$(repCheckVer)"
	rm -rf "check_rmt_repos_$(repCheckVer)"

tar-repo-sig:
	mkdir "monitoring-plugins-repo-signatures-$(repoSigVer)"
	cp check_repo_signatures LICENSE "monitoring-plugins-repo-signatures-$(repoSigVer)"
	tar -cjf "monitoring-plugins-repo-signatures-$(repoSigVer).tar.bz2" "monitoring-plugins-repo-signatures-$(repoSigVer)"
	rm -rf "monitoring-plugins-repo-signatures-$(repoSigVer)"

tar-old-files:
	mkdir "monitoring-plugins-old-files-$(oldFilesVer)"
	cp check_old_files LICENSE "monitoring-plugins-old-files-$(oldFilesVer)"
	tar -cjf "monitoring-plugins-old-files-$(oldFilesVer).tar.bz2" "monitoring-plugins-old-files-$(oldFilesVer)"
	rm -rf "monitoring-plugins-old-files-$(oldFilesVer)"
