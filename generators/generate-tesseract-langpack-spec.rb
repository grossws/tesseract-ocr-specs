#!/usr/bin/env ruby

require 'erb'

@langs = {
  'eng' => 'English language',
  'rus' => 'Russian language',
  'grc' => 'Ancient Greek language',
  'epo_alt' => 'Esperanto alternative language',
  'ukr' => 'Ukrainian language',
  'tur' => 'Turkish language',
  'tha' => 'Thai language',
  'tgl' => 'Tagalog language',
  'tel' => 'Telugu language',
  'tam' => 'Tamil language',
  'swe' => 'Swedish language',
  'swa' => 'Swahili language',
  'srp' => 'Serbian (Latin) language',
  'sqi' => 'Albanian language',
  'spa_old' => 'Spanish (Old) language',
  'spa' => 'Spanish language',
  'slv' => 'Slovenian language',
  'slk' => 'Slovakian language',
  'ron' => 'Romanian language',
  'por' => 'Portuguese language',
  'pol' => 'Polish  language',
  'nor' => 'Norwegian language',
  'nld' => 'Dutch language',
  'msa' => 'Malay language',
  'mlt' => 'Maltese language',
  'mkd' => 'Macedonian language',
  'mal' => 'Malayalam language',
  'lit' => 'Lithuanian language',
  'lav' => 'Latvian language',
  'kor' => 'Korean language',
  'kan' => 'Kannada language',
  'ita_old' => 'Italian (Old) language',
  'ita' => 'Italian language',
  'isl' => 'Icelandic language',
  'ind' => 'Indonesian language',
  'chr' => 'Cherokee language',
  'hun' => 'Hungarian  language',
  'hrv' => 'Croatian language',
  'hin' => 'Hindi language',
  'heb' => 'Hebrew language',
  'glg' => 'Galician language',
  'frm' => 'Middle French (ca. 1400-1600)  language',
  'frk' => 'Frankish language',
  'fra' => 'French language',
  'fin' => 'Finnish language',
  'eus' => 'Basque language',
  'est' => 'Estonian language',
  'equ' => 'Math / equation detection',
  'epo' => 'Esperanto language',
  'enm' => 'Middle English (1100-1500) language',
  'ell' => 'Greek language',
  'deu' => 'German language',
  'dan' => 'Danish language',
  'ces' => 'Czech language',
  'cat' => 'Catalan language',
  'bul' => 'Bulgarian language',
  'ben' => 'Bengali language',
  'bel' => 'Belarusian language',
  'aze' => 'Azerbaijani language',
  'ara' => 'Arabic language',
  'afr' => 'Afrikaans language',
  'jpn' => 'Japanese language',
  'chi_sim' => 'Chinese (Simplified) language',
  'chi_tra' => 'Chinese (Traditional) language',
  'vie' => 'Vietnamese language',
  'dan-frak' => 'Danish (Fraktur) language',
  'deu-frak' => 'German (Fraktur) language',
  'slk-frak' => 'Slovakian (Fraktur) language'
}

@leptonica_version = '1.69'
@tesseract_version = '3.02.02'
@tesseract_langpack_version = '3.02'

File.open(File.expand_path("../../utils/download_sources.sh", __FILE__), "w") do |f|
  f.write ERB.new(File.read(File.expand_path("../download-sources.sh.erb", __FILE__)), nil, '-').result
end
File.chmod(0755, File.expand_path("../../utils/download_sources.sh", __FILE__))

@langs.delete 'eng' # English is included in tesseract package
File.open(File.expand_path("../../specs/tesseract-langpack.spec", __FILE__), "w") do |f|
  f.write ERB.new(File.read(File.expand_path("../tesseract-langpack.spec.erb", __FILE__)), nil, '-').result
end

