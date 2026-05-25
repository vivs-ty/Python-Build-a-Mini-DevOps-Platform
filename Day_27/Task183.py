# Task 183: Tag cloud resources and filter them by tags.

import random

# Simulate cloud resources with tags
resources = [
    {"id": 1, "name": "Instance-1", "tags": {"environment": "production", "team": "backend"}},
    {"id": 2, "name": "Instance-2", "tags": {"environment": "development", "team": "frontend"}},
    {"id": 3, "name": "Instance-3", "tags": {"environment": "production", "team": "backend"}},
]

# Function to filter resources by tags
def filter_resources_by_tags(resources_list, filter_tags):
    return [resource for resource in resources_list if all(resource["tags"].get(key) == value for key, value in filter_tags.items())]

# Example usage
filtered_resources = filter_resources_by_tags(resources, {"environment": "production"})
print("Filtered Resources:")
for resource in filtered_resources:
    print(f" - {resource['name']}")