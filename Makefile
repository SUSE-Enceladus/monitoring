dirEmptyVer =  $(shell rpm -q --specfile --qf '%{VERSION}' monitoring-plugins-dir-empty.spec)
procHangVer = $(shell rpm -q --specfile --qf '%{VERSION}' monitoring-plugins-proc-timed-hang.spec)
repoSigVer = $(shell rpm -q --specfile --qf '%{VERSION}' monitoring-plugins-repo-signatures.spec)

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

tar-repo-sig:
	mkdir "monitoring-plugins-repo-signatures-$(repoSigVer)"
	cp check_repo_signatures LICENSE "monitoring-plugins-repo-signatures-$(repoSigVer)"
	tar -cjf "monitoring-plugins-repo-signatures-$(repoSigVer).tar.bz2" "monitoring-plugins-repo-signatures-$(repoSigVer)"
	rm -rf "monitoring-plugins-repo-signatures-$(repoSigVer)"
