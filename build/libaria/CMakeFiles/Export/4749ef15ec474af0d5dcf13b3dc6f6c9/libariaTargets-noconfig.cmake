#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "libaria::Aria" for configuration ""
set_property(TARGET libaria::Aria APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(libaria::Aria PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libAria.so"
  IMPORTED_SONAME_NOCONFIG "libAria.so"
  )

list(APPEND _cmake_import_check_targets libaria::Aria )
list(APPEND _cmake_import_check_files_for_libaria::Aria "${_IMPORT_PREFIX}/lib/libAria.so" )

# Import target "libaria::ArNetworking" for configuration ""
set_property(TARGET libaria::ArNetworking APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(libaria::ArNetworking PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libArNetworking.so"
  IMPORTED_SONAME_NOCONFIG "libArNetworking.so"
  )

list(APPEND _cmake_import_check_targets libaria::ArNetworking )
list(APPEND _cmake_import_check_files_for_libaria::ArNetworking "${_IMPORT_PREFIX}/lib/libArNetworking.so" )

# Import target "libaria::omron_robot_cli" for configuration ""
set_property(TARGET libaria::omron_robot_cli APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(libaria::omron_robot_cli PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/bin/omron_robot_cli"
  )

list(APPEND _cmake_import_check_targets libaria::omron_robot_cli )
list(APPEND _cmake_import_check_files_for_libaria::omron_robot_cli "${_IMPORT_PREFIX}/bin/omron_robot_cli" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
