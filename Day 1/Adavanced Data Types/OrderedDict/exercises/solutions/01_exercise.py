from collections import OrderedDict
from typing import List, Dict, Optional

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
        self.sections = OrderedDict()
    
    def add_section(self, section: Dict, after: Optional[str] = None):
        """Add a section, optionally after another section."""
        if after is not None and after in self.sections:
            # Create new OrderedDict with desired order
            new_sections = OrderedDict()
            for sid, existing_section in self.sections.items():
                new_sections[sid] = existing_section
                if sid == after:
                    new_sections[section['id']] = section
            if section['id'] not in new_sections:
                new_sections[section['id']] = section
            self.sections = new_sections
        else:
            self.sections[section['id']] = section
    
    def remove_section(self, section_id: str) -> bool:
        """Remove a section."""
        if section_id in self.sections:
            del self.sections[section_id]
            return True
        return False
    
    def move_section(self, section_id: str, after: Optional[str]) -> bool:
        """Move a section to a new position."""
        if section_id in self.sections:
            section = self.sections.pop(section_id)
            self.add_section(section, after)
            return True
        return False
    
    def get_required_sections(self) -> List[Dict]:
        """Get all required sections."""
        return [
            section for section in self.sections.values()
            if section['required']
        ]
    
    def validate_order(self) -> List[str]:
        """Validate section order and return any issues."""
        issues = []
        required_found = False
        
        for section in self.sections.values():
            if section['required']:
                required_found = True
            elif not required_found and not section['required']:
                issues.append(
                    f"Optional section '{section['title']}' appears before "
                    "required sections"
                )
        
        required_sections = self.get_required_sections()
        if not required_sections:
            issues.append("No required sections found")
        
        return issues
    
    def get_all_sections(self) -> List[Dict]:
        """Get all sections in order."""
        return list(self.sections.values())

def implement_section_manager(sections: List[Dict]) -> Dict:
    """Implement a document section manager using OrderedDict."""
    manager = SectionManager()
    
    # Add sections
    for section in sections:
        manager.add_section(section)
    
    # Demonstrate operations
    manager.move_section('summary', 'header')
    manager.add_section({
        'id': 'references',
        'title': 'References',
        'content': 'Document references',
        'required': False
    }, 'appendix')
    
    return {
        'all_sections': manager.get_all_sections(),
        'required_sections': manager.get_required_sections(),
        'validation_issues': manager.validate_order()
    }
