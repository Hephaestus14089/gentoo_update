report_2_packages = [
    'processed packages:',
    '--- dev-libs/libffi 3.4.4-r1:0/8->3.4.4-r2:0/8',
    '--- sys-apps/baselayout 2.14->2.14-r1',
    '--- sys-apps/hwdata 0.375->0.376',
    '--- dev-libs/ell 0.56->0.58',
    '--- acct-group/pipewire ->0-r1',
    '--- media-libs/libfreeaptx ->0.1.1-r1',
    '--- net-analyzer/traceroute 2.1.1->2.1.3',
    '--- sys-kernel/linux-firmware 20231030->20231211',
    '--- dev-libs/vala-common 0.56.8->0.56.14',
    '--- net-libs/libnsl 2.0.0-r1:0/3->2.0.1:0/3',
    '--- sys-libs/zlib 1.3-r1:0/1->1.3-r2:0/1',
    '--- media-libs/fdk-aac ->2.0.2:0/2',
    '--- media-libs/tiff 4.5.1:0/6->4.6.0:0/6',
    '--- media-libs/x264 0.0.20220222:0/164->0.0.20231114-r1:0/164',
    '--- media-fonts/fontawesome 5.15.3:0/5->6.1.1:0/6',
    '--- dev-libs/gobject-introspection-common 1.76.1->1.78.1',
    '--- dev-lang/perl 5.38.0-r1:0/5.38->5.38.2-r1:0/5.38',
    '--- dev-libs/openssl 3.0.11:0/3->3.0.12:0/3',
    '--- app-admin/eselect 1.4.27->1.4.27-r1',
    '--- app-eselect/eselect-pinentry 0.7.2-r1->0.7.3',
    '--- virtual/perl-Math-BigInt-FastCalc ->0.501.300',
    '--- virtual/perl-bignum ->0.660.0',
    '--- virtual/perl-Math-BigRat ->0.262.400',
    '--- virtual/perl-Math-Complex ->1.620.0',
    '--- perl-core/Math-BigInt ->1.999.842',
    '--- virtual/perl-Math-BigInt ->1.999.842',
    '--- virtual/perl-Unicode-Collate ->1.310.0-r1',
    '--- media-libs/libvpx 1.13.1:0/8->1.13.1-r1:0/8',
    '--- sys-auth/passwdqc 2.0.3->2.0.3-r1',
    '--- sys-apps/kbd 2.6.1->2.6.4',
    '--- dev-ruby/google-protobuf ->3.21.12:3',
    '--- dev-ruby/googleapis-common-protos-types ->1.8.0:1',
    '--- dev-ruby/excon 0.93.1->0.104.0',
    '--- dev-ruby/grpc ->1.54.0',
    '--- dev-util/ninja 1.11.1-r2->1.11.1-r3',
    '--- app-alternatives/ninja ->1',
    '--- sys-fs/fuse 3.16.1:3->3.16.2:3',
    '--- gnome-base/gnome-core-libs 41.3:3.0->44.4:3.0',
    '--- sys-apps/iproute2 6.5.0->6.6.0',
    '--- sys-kernel/gentoo-kernel-bin 6.1.53-r1:6.1.53->6.1.67:6.1.67',
    '--- virtual/dist-kernel 6.1.66:0/6.1.66->6.1.67:0/6.1.67',
    '--- app-admin/sudo 1.9.14_p3->1.9.15_p2',
    '--- app-editors/vim-core 9.0.1777->9.0.2092',
    '--- dev-db/sqlite 3.43.2:3->3.44.2-r1:3',
    '--- sys-apps/kmod 30-r1->31',
    '--- sys-apps/debianutils 5.8->5.14',
    '--- net-misc/openssh 9.4_p1-r1->9.6_p1-r1',
    '--- dev-util/colm 0.14.7->0.14.7-r3',
    '--- app-misc/ca-certificates 20230311.3.90->20230311.3.93',
    '--- dev-util/ragel 7.0.4->7.0.4-r2',
    '--- app-emulation/virtualbox-modules ->7.0.10:0/7.0',
    '--- gnome-base/gnome-light 40.0:2.0->44.4:2.0',
    '--- media-libs/openjpeg 2.5.0-r5:2/7->2.5.0-r6:2/7',
    '--- app-text/qpdf 11.6.3:0/11->11.6.3-r1:0/11',
    '--- dev-util/spirv-headers 1.3.261->1.3.268',
    '--- dev-util/vulkan-headers 1.3.261->1.3.268',
    '--- media-libs/libldac ->2.0.2.3-r1',
    '--- dev-util/spirv-tools 1.3.261->1.3.268',
    '--- media-libs/vulkan-loader 1.3.261->1.3.268',
    '--- dev-util/glslang 1.3.261:0/12->1.3.268-r2:0/13',
    '--- app-text/ghostscript-gpl 10.02.0:0/10.02->10.02.1:0/10.02',
    '--- x11-terms/alacritty 0.12.2->0.12.3',
    '--- app-text/mupdf 1.22.0:0/1.22.0->1.23.3:0/1.23.3',
    '--- dev-libs/gmp 6.3.0:0/10.4->6.3.0-r1:0/10.4',
    '--- sys-devel/gettext 0.21.1->0.22.4',
    '--- dev-libs/libxslt 1.1.38->1.1.39',
    '--- dev-libs/libgpg-error 1.47->1.47-r1',
    '--- sys-devel/binutils 2.40-r9:2.40->2.41-r2:2.41',
    '--- dev-libs/elfutils 0.189-r4->0.190',
    '--- sys-apps/texinfo 7.0.3->7.1-r1',
    '--- app-editors/vim 9.0.1777->9.0.2092',
    '--- sys-libs/binutils-libs 2.40-r7:0/2.40->2.41-r2:0/2.41.0',
    '--- dev-util/dialog 1.3.20230209:0/15->1.3.20231002:0/15',
    '--- sys-apps/gawk 5.2.2->5.3.0',
    '--- dev-libs/libksba 1.6.4-r1->1.6.5',
    '--- app-arch/libarchive 3.7.1:0/13->3.7.2:0/13',
    '--- sys-apps/groff 1.22.4->1.23.0',
    '--- sys-process/lsof 4.98.0-r1->4.99.0',
    '--- dev-lang/vala 0.56.8:0.56->0.56.14:0.56',
    '--- dev-libs/libical 3.0.16:0/3->3.0.17:0/3',
    '--- dev-python/hatchling 1.18.0->1.20.0',
    '--- dev-util/gdbus-codegen 2.76.4->2.78.3',
    '--- dev-libs/glib 2.76.4:2->2.78.3:2',
    '--- dev-lang/python 3.11.6:3.11->3.11.7:3.11',
    '--- sys-apps/systemd 254.5-r1:0/2->254.7:0/2',
    '--- net-wireless/bluez 5.68:0/3->5.70-r1:0/3',
    '--- dev-libs/gobject-introspection 1.76.1->1.78.1',
    '--- sys-apps/portage 3.0.56-r1->3.0.59',
    '--- net-print/cups-filters ->1.28.17-r2',
    '--- dev-util/glib-utils 2.76.4->2.78.3',
    '--- x11-base/xorg-server 21.1.9:0/21.1.9->21.1.10-r1:0/21.1.10',
    '--- net-wireless/iwd 2.4->2.8-r2',
    '--- sys-kernel/dracut 059-r5->059-r7',
    '--- dev-python/jaraco-text 3.11.1-r1->3.12.0',
    '--- dev-python/platformdirs 4.0.0->4.1.0',
    '--- dev-python/wheel 0.41.3->0.42.0',
    '--- dev-python/typing-extensions 4.8.0->4.9.0',
    '--- dev-python/pathspec 0.11.2->0.12.1',
    '--- dev-python/cython 3.0.5->3.0.6',
    '--- net-libs/glib-networking 2.76.1->2.78.0',
    '--- dev-lang/spidermonkey 102.10.0:102->102.15.0:102',
    '--- dev-cpp/glibmm 2.76.0:2.68->2.78.0:2.68',
    '--- dev-python/hatch-vcs 0.3.0->0.4.0',
    '--- dev-python/argcomplete 3.1.6->3.2.1',
    '--- sys-auth/polkit 122-r1->123',
    '--- dev-python/pygobject 3.44.1:3->3.46.0:3',
    '--- x11-drivers/xf86-input-libinput ->1.4.0',
    '--- net-libs/webkit-gtk 2.42.1-r410:4.1/0->2.42.3-r410:4.1/0',
    '--- x11-drivers/xf86-video-amdgpu ->23.0.0',
    '--- x11-drivers/xf86-video-ati ->22.0.0',
    '--- x11-drivers/xf86-video-dummy ->0.4.1',
    '--- x11-drivers/xf86-video-fbdev ->0.5.0-r1',
    '--- x11-drivers/xf86-video-nouveau ->1.0.17',
    '--- x11-drivers/xf86-video-vesa ->2.6.0',
    '--- app-editors/vscode 1.84.2->1.85.1',
    '--- app-portage/gentoolkit 0.6.3->0.6.3-r1',
    '--- www-client/brave-bin 1.61.101->1.61.109',
    '--- www-client/firefox-bin 120.0.1:rapid->121.0:rapid',
    '--- dev-libs/libgee 0.20.6:0.8/2->0.20.6-r1:0.8/2',
    '--- gnome-base/gvfs 1.50.6->1.52.1',
    '--- media-video/pipewire ->0.3.80:0/0.4',
    '--- media-video/wireplumber ->0.4.14:0/0.4',
    '--- sys-apps/xdg-desktop-portal 1.16.0-r1->1.18.2',
    '',
    'Non-ebuild packages',
    '--- dev-libs/gobject-introspection-1.78.1 blocked '
    'dev-libs/gobject-introspection-common-1.78.1',
    ''
]
