import commands
import sublime, sublime_plugin

class XmllintCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.run_command("save")
    filename=self.view.file_name()

    xml = commands.getoutput("xmllint --format " + filename)

    if len(xml) > 0:
      self.view.replace(edit, sublime.Region(0, self.view.size()), xml.decode('utf-8'))
      self.view.set_syntax_file('Packages/XML/XML.tmLanguage')
      #sublime.set_timeout(self.save, 100)
