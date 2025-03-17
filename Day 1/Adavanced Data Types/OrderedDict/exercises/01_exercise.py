from collections import OrderedDict
from datetime import datetime
from typing import List, Dict, Optional, Any, Callable
import json

document_sections = [
    {
        'id': 'header',
        'title': 'Document Header',
        'content': 'Company letterhead and document title',
        'required': True
    },
    {
        'id': 'summary',
        'title': 'Executive Summary',
        'content': 'Brief overview of the document',
        'required': True
    },
    {
        'id': 'details',
        'title': 'Detailed Content',
        'content': 'Main document content',
        'required': True
    },
    {
        'id': 'appendix',
        'title': 'Appendices',
        'content': 'Additional supporting information',
        'required': False
    }
]

class SectionManager:
    """Manages document sections and their order."""
    
    def __init__(self):
        # TODO 1: Initialize the sections using OrderedDict
        pass
    
    def add_section(self, section: Dict, after: Optional[str] = None):
        """Add a section, optionally after another section."""
        # TODO 2: Implement add_section
        # - If after is None, just add to end
        # - If after is specified, add section after that section
        # Hint: For after, create new OrderedDict with desired order
        pass
    
    def move_section(self, section_id: str, after: Optional[str]) -> bool:
        """Move a section to a new position."""
        if section_id not in self.sections:
            return False
            
        # TODO 3: Implement move using add_section
        # Hint: Remove section and add it back in new position
        return True
    
    def get_required_sections(self) -> List[Dict]:
        """Get all required sections."""
        return [section for section in self.sections.values() if section['required']]

def implement_section_manager(sections: List[Dict]) -> Dict:
    """
    Implement a document section manager using OrderedDict.
    
    The manager should:
    1. Maintain section order
    2. Allow moving sections
    3. Track required vs optional sections
    """
    manager = SectionManager()
    
    # Add initial sections
    for section in sections:
        manager.add_section(section)
    
    # Test moving a section
    manager.move_section('summary', 'header')
    
    return {
        'all_sections': list(manager.sections.values()),
        'required_sections': manager.get_required_sections()
    }
