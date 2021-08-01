#!/usr/bin/python3
import mdstat

mdjson = mdstat.parse()

lines = []
for md in mdjson['devices']:
  mddev = mdjson['devices'][md]
  ln = []
  ln.append('mdstat,')
  ln.append('personality=' + mddev['personality'])
  ln.append(' ')
  ln.append('active=' + str(int(mddev['active'])) + 'i,')
  ln.append('read_only=' + str(int(mddev['read_only'])) + 'i,')
  ln.append('raid_disks=' + str(int(mddev['status']['raid_disks'])) + 'i,')
  ln.append('non_degraded_disks=' + str(int(mddev['status']['non_degraded_disks'])) + 'i')
  lines.append(''.join(ln))
  if mddev['resync']:
      ln = []
      ln.append('mdstat-resync,')
      ln.append('md=' + md + ' ')
      ln.append('operation="' + mddev['resync']['operation'] + '",')
      ln.append('progress=' + str(float(mddev['resync']['progress'][:-1])) + ',')
      ln.append('finish_s=' + str(float(mddev['resync']['finish'][:-3]) * 60) + ',')
      ln.append('speed_kbs=' + str(int(mddev['resync']['speed'][:-5])) + 'i,')
      ln.append('resynced=' + str(int(mddev['resync']['resynced'])) + 'i,')
      ln.append('total=' + str(int(mddev['resync']['total'])) + 'i')
      lines.append(''.join(ln))
  for disk in mddev['disks']:
    disks = mddev['disks']
    ln = []
    ln.append('mdstat-disk,')
    ln.append('md=' + md + ',')
    ln.append('disk=' + disk + ',')
    ln.append('number=' + str(int(disks[disk]['number'])))
    ln.append(' ')
    ln.append('faulty=' + str(int(disks[disk]['faulty'])) + 'i,')
    ln.append('spare=' + str(int(disks[disk]['spare'])) + 'i,')
    ln.append('replacement=' + str(int(disks[disk]['replacement'])) + 'i,')
    ln.append('write_mostly=' + str(int(disks[disk]['write_mostly'])) + 'i,')
    ln.append('replacement=' + str(int(disks[disk]['replacement'])) + 'i')
    lines.append(''.join(ln))

if len(lines):
  print('\n'.join(lines))

