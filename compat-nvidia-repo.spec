Name:           compat-nvidia-repo
Version:        410.93
Epoch:          3
Release:        1%{?dist}
Summary:        Compatibility package required by official CUDA packages
License:        NVIDIA License
URL:            https://developer.nvidia.com/cuda-toolkit

BuildArch:      noarch

Requires:       nvidia-driver >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-driver-NVML >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-driver-NvFBCOpenGL >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-driver-cuda >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-driver-cuda-libs >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-driver-devel >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-driver-libs >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-kmod >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-libXNVCtrl >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-libXNVCtrl-devel >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-modprobe >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-persistenced >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-settings >= %{?epoch:%{epoch}:}%{version}
Requires:       nvidia-xconfig >= %{?epoch:%{epoch}:}%{version}

Provides:       cuda-drivers >= %{?epoch:%{epoch}:}%{version}
Provides:       nvidia-drivers >= %{?epoch:%{epoch}:}%{version}

%description
Nvidia drivers metapackage required by official CUDA packages. It pulls in all
Nvidia driver components.

%files
# Empty

%changelog
* Sun Feb  3 2019 Simone Caronni <negativo17@gmail.com> - 3:410.93-1
- First build.