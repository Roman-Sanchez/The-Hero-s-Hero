import xml.etree.ElementTree as ET


'''
	xmlSpriteParser will parse an xml file that contains image coordinate data 
	in a sprites sheet.

	Example xml file:

<?xml version="1.0"?>
<!-- Generated by darkFunction Editor (www.darkfunction.com) -->
<img name="MonoeyesOptimized.png" w="512" h="512">
  <definitions>
    <dir name="/">
      <spr name="0" x="0" y="0" w="61" h="172"/>
      <spr name="1" x="0" y="172" w="61" h="172"/>
      <spr name="2" x="61" y="0" w="56" h="172"/>
      <spr name="3" x="232" y="0" w="54" h="172"/>
      <spr name="4" x="117" y="0" w="58" h="172"/>
      <spr name="5" x="175" y="0" w="57" h="172"/>
      <spr name="6" x="61" y="172" w="56" h="172"/>
      <spr name="7" x="286" y="0" w="54" h="172"/>
      <spr name="8" x="396" y="172" w="53" h="172"/>
      <spr name="9" x="340" y="0" w="55" h="172"/>
      <spr name="10" x="395" y="0" w="57" h="172"/>
      <spr name="11" x="452" y="0" w="58" h="172"/>
      <spr name="12" x="117" y="172" w="58" h="172"/>
      <spr name="13" x="175" y="172" w="55" h="172"/>
      <spr name="14" x="230" y="172" w="55" h="172"/>
      <spr name="15" x="285" y="172" w="57" h="172"/>
      <spr name="16" x="342" y="172" w="54" h="172"/>
    </dir>
  </definitions>
</img>

'''
class XmlSpriteParser(object):

	def __init__(self, fileName):
		self.okayToUpdate = True
		self.numImages = 0
		self.fileName = fileName
		self.tree = ET.parse(self.fileName)
		self.root = self.tree.getroot()
		# will be a dictionary of dictionaries
		# indexed like so, imagesCoors[0]['item in sub-dictionary ex. 'xCoor'']
		self.imagesCoors = {}
		self.update()
		self.findNumImages()

	def update(self):

		# Controls whether the getImageInfo is called. This method should only 
		# Be called once 
		if (self.okayToUpdate):
			self.getImageInfo()
			self.okayToUpdate = False
		
	def getImageInfo(self):

		''' This iterator will append a dictionary to the member dictionary, 
			imagesCoors.

			for child in self.root.iter('spr'): # iterator through the root 
												# element and find all the 
												# elements named "spr"
				
				# append a dictionary to the member dictionary (imagesCoors) 
				# with all the image info from the current "spr" element.
				# use the int() function to convert the child.get('name') from a
				# string to an int so that the dictionary may be indexed
				# using an integer. each child.get() function is getting a 
				#different attribute from the current element
				self.imagesCoors[int(child.get('name'))] = {"xCoor": child.get('x'), 
					"yCoor": child.get('y'), "width": child.get('w'), 
					"height": child.get('h')}

		'''
		for child in self.root.iter('spr'):
			self.imagesCoors[int(child.get('name'))] = {"xCoor": child.get('x'), 
				"yCoor": child.get('y'), "width": child.get('w'), 
				"height": child.get('h')}
	
	# gets the number of "spr" elements in the xml. This number represents the 
	# number of images that are in the cooresponding sprite sheet
	def findNumImages(self):
		self.numImages = len(self.imagesCoors)

# tests the XmlSpriteParser
def main():

	test = XmlSpriteParser('MetalSlugSprites/newSpriteSheet.sprites')
	print test.okayToUpdate
	test.update()
	print test.imagesCoors[16]['width']
	print test.okayToUpdate
	print test.numImages

	tree = ET.parse('MetalSlugSprites/newSpriteSheet.sprites')
	root = tree.getroot()

if __name__ == "__main__":
	main()