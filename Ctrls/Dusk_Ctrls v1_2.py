keyconfig_version = (4, 0, 36)
keyconfig_data = \
[("3D View",
  {"space_type": 'VIEW_3D', "region_type": 'WINDOW'},
  {"items":
   [("view3d.rotate_canvas", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("view3d.rotate_canvas", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("view3d.cursor3d", {"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True}, None),
    ("transform.translate",
     {"type": 'RIGHTMOUSE', "value": 'CLICK_DRAG', "shift": True},
     {"properties":
      [("cursor_transform", True),
       ("release_confirm", True),
       ],
      },
     ),
    ("view3d.localview", {"type": 'NUMPAD_SLASH', "value": 'PRESS'}, None),
    ("view3d.localview", {"type": 'SLASH', "value": 'PRESS'}, None),
    ("view3d.localview", {"type": 'MOUSESMARTZOOM', "value": 'ANY'}, None),
    ("view3d.localview_remove_from", {"type": 'NUMPAD_SLASH', "value": 'PRESS', "alt": True}, None),
    ("view3d.localview_remove_from", {"type": 'SLASH', "value": 'PRESS', "alt": True}, None),
    ("view3d.move", {"type": 'LEFTMOUSE', "value": 'CLICK_DRAG', "shift": True, "alt": True}, None),
    ("view3d.rotate", {"type": 'LEFTMOUSE', "value": 'CLICK_DRAG', "alt": True}, None),
    ("view3d.move", {"type": 'TRACKPADPAN', "value": 'ANY', "shift": True}, None),
    ("view3d.zoom", {"type": 'LEFTMOUSE', "value": 'CLICK_DRAG', "ctrl": True, "alt": True}, None),
    ("view3d.dolly", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "shift": True, "ctrl": True}, None),
    ("view3d.view_selected",
     {"type": 'NUMPAD_PERIOD', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("use_all_regions", True),
       ],
      },
     ),
    ("view3d.view_selected",
     {"type": 'NUMPAD_PERIOD', "value": 'PRESS'},
     {"properties":
      [("use_all_regions", False),
       ],
      },
     ),
    ("view3d.smoothview", {"type": 'TIMER1', "value": 'ANY', "any": True}, None),
    ("view3d.zoom", {"type": 'TRACKPADZOOM', "value": 'ANY'}, None),
    ("view3d.zoom", {"type": 'TRACKPADPAN', "value": 'ANY', "ctrl": True}, None),
    ("view3d.zoom",
     {"type": 'NUMPAD_PLUS', "value": 'PRESS', "repeat": True},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'NUMPAD_MINUS', "value": 'PRESS', "repeat": True},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'EQUAL', "value": 'PRESS', "ctrl": True, "repeat": True},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'MINUS', "value": 'PRESS', "ctrl": True, "repeat": True},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'WHEELINMOUSE', "value": 'PRESS'},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.zoom",
     {"type": 'WHEELOUTMOUSE', "value": 'PRESS'},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.dolly",
     {"type": 'NUMPAD_PLUS', "value": 'PRESS', "shift": True, "repeat": True},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.dolly",
     {"type": 'NUMPAD_MINUS', "value": 'PRESS', "shift": True, "repeat": True},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.dolly",
     {"type": 'EQUAL', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},
     {"properties":
      [("delta", 1),
       ],
      },
     ),
    ("view3d.dolly",
     {"type": 'MINUS', "value": 'PRESS', "shift": True, "ctrl": True, "repeat": True},
     {"properties":
      [("delta", -1),
       ],
      },
     ),
    ("view3d.view_center_camera", {"type": 'HOME', "value": 'PRESS'}, None),
    ("view3d.view_center_lock", {"type": 'HOME', "value": 'PRESS'}, None),
    ("view3d.view_all",
     {"type": 'HOME', "value": 'PRESS'},
     {"properties":
      [("center", False),
       ],
      },
     ),
    ("view3d.view_all",
     {"type": 'HOME', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("use_all_regions", True),
       ("center", False),
       ],
      },
     ),
    ("view3d.view_all",
     {"type": 'C', "value": 'PRESS', "shift": True},
     {"properties":
      [("center", True),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'ACCENT_GRAVE', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_view_pie'),
       ],
      },
     ),
    ("view3d.navigate", {"type": 'ACCENT_GRAVE', "value": 'PRESS', "shift": True}, None),
    ("view3d.view_camera", {"type": 'NUMPAD_0', "value": 'PRESS'}, None),
    ("view3d.view_axis",
     {"type": 'NUMPAD_1', "value": 'PRESS'},
     {"properties":
      [("type", 'FRONT'),
       ],
      },
     ),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_2', "value": 'PRESS', "repeat": True},
     {"properties":
      [("type", 'ORBITDOWN'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_3', "value": 'PRESS'},
     {"properties":
      [("type", 'RIGHT'),
       ],
      },
     ),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_4', "value": 'PRESS', "repeat": True},
     {"properties":
      [("type", 'ORBITLEFT'),
       ],
      },
     ),
    ("view3d.view_persportho", {"type": 'NUMPAD_5', "value": 'PRESS'}, None),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_6', "value": 'PRESS', "repeat": True},
     {"properties":
      [("type", 'ORBITRIGHT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_7', "value": 'PRESS'},
     {"properties":
      [("type", 'TOP'),
       ],
      },
     ),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_8', "value": 'PRESS', "repeat": True},
     {"properties":
      [("type", 'ORBITUP'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_1', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("type", 'BACK'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_3', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("type", 'LEFT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_7', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("type", 'BOTTOM'),
       ],
      },
     ),
    ("view3d.view_pan",
     {"type": 'NUMPAD_2', "value": 'PRESS', "ctrl": True, "repeat": True},
     {"properties":
      [("type", 'PANDOWN'),
       ],
      },
     ),
    ("view3d.view_pan",
     {"type": 'NUMPAD_4', "value": 'PRESS', "ctrl": True, "repeat": True},
     {"properties":
      [("type", 'PANLEFT'),
       ],
      },
     ),
    ("view3d.view_pan",
     {"type": 'NUMPAD_6', "value": 'PRESS', "ctrl": True, "repeat": True},
     {"properties":
      [("type", 'PANRIGHT'),
       ],
      },
     ),
    ("view3d.view_pan",
     {"type": 'NUMPAD_8', "value": 'PRESS', "ctrl": True, "repeat": True},
     {"properties":
      [("type", 'PANUP'),
       ],
      },
     ),
    ("view3d.view_roll",
     {"type": 'NUMPAD_4', "value": 'PRESS', "shift": True, "repeat": True},
     {"properties":
      [("type", 'LEFT'),
       ],
      },
     ),
    ("view3d.view_roll",
     {"type": 'NUMPAD_6', "value": 'PRESS', "shift": True, "repeat": True},
     {"properties":
      [("type", 'RIGHT'),
       ],
      },
     ),
    ("view3d.view_orbit",
     {"type": 'NUMPAD_9', "value": 'PRESS'},
     {"properties":
      [("angle", 3.1415927),
       ("type", 'ORBITRIGHT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_1', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'FRONT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_3', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'RIGHT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_7', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'TOP'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_1', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("type", 'BACK'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_3', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("type", 'LEFT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NUMPAD_7', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("type", 'BOTTOM'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'MIDDLEMOUSE', "value": 'CLICK_DRAG', "alt": True, "direction": 'NORTH'},
     {"properties":
      [("type", 'TOP'),
       ("relative", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'MIDDLEMOUSE', "value": 'CLICK_DRAG', "alt": True, "direction": 'SOUTH'},
     {"properties":
      [("type", 'BOTTOM'),
       ("relative", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'MIDDLEMOUSE', "value": 'CLICK_DRAG', "alt": True, "direction": 'EAST'},
     {"properties":
      [("type", 'RIGHT'),
       ("relative", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'MIDDLEMOUSE', "value": 'CLICK_DRAG', "alt": True, "direction": 'WEST'},
     {"properties":
      [("type", 'LEFT'),
       ("relative", True),
       ],
      },
     ),
    ("view3d.view_center_pick", {"type": 'MIDDLEMOUSE', "value": 'CLICK', "alt": True}, None),
    ("view3d.ndof_orbit_zoom", {"type": 'NDOF_MOTION', "value": 'ANY'}, None),
    ("view3d.ndof_orbit", {"type": 'NDOF_MOTION', "value": 'ANY', "ctrl": True}, None),
    ("view3d.ndof_pan", {"type": 'NDOF_MOTION', "value": 'ANY', "shift": True}, None),
    ("view3d.ndof_all", {"type": 'NDOF_MOTION', "value": 'ANY', "shift": True, "ctrl": True}, None),
    ("view3d.view_selected",
     {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'},
     {"properties":
      [("use_all_regions", False),
       ],
      },
     ),
    ("view3d.view_roll",
     {"type": 'NDOF_BUTTON_ROLL_CW', "value": 'PRESS'},
     {"properties":
      [("angle", 1.5707964),
       ],
      },
     ),
    ("view3d.view_roll",
     {"type": 'NDOF_BUTTON_ROLL_CCW', "value": 'PRESS'},
     {"properties":
      [("angle", -1.5707964),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_FRONT', "value": 'PRESS'},
     {"properties":
      [("type", 'FRONT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_BACK', "value": 'PRESS'},
     {"properties":
      [("type", 'BACK'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_LEFT', "value": 'PRESS'},
     {"properties":
      [("type", 'LEFT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_RIGHT', "value": 'PRESS'},
     {"properties":
      [("type", 'RIGHT'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_TOP', "value": 'PRESS'},
     {"properties":
      [("type", 'TOP'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_BOTTOM', "value": 'PRESS'},
     {"properties":
      [("type", 'BOTTOM'),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_FRONT', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'FRONT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_RIGHT', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'RIGHT'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.view_axis",
     {"type": 'NDOF_BUTTON_TOP', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'TOP'),
       ("align_active", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK'},
     {"properties":
      [("deselect_all", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True},
     {"properties":
      [("toggle", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "ctrl": True},
     {"properties":
      [("center", True),
       ("object", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "alt": True},
     {"properties":
      [("enumerate", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True, "ctrl": True},
     {"properties":
      [("toggle", True),
       ("center", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "ctrl": True, "alt": True},
     {"properties":
      [("center", True),
       ("enumerate", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True, "alt": True},
     {"properties":
      [("toggle", True),
       ("enumerate", True),
       ],
      },
     ),
    ("view3d.select",
     {"type": 'LEFTMOUSE', "value": 'CLICK', "shift": True, "ctrl": True, "alt": True},
     {"properties":
      [("toggle", True),
       ("center", True),
       ("enumerate", True),
       ],
      },
     ),
    ("view3d.select_box", {"type": 'B', "value": 'PRESS'}, None),
    ("view3d.select_lasso",
     {"type": 'RIGHTMOUSE', "value": 'CLICK_DRAG', "ctrl": True},
     {"properties":
      [("mode", 'ADD'),
       ],
      },
     ),
    ("view3d.select_lasso",
     {"type": 'RIGHTMOUSE', "value": 'CLICK_DRAG', "shift": True, "ctrl": True},
     {"properties":
      [("mode", 'SUB'),
       ],
      },
     ),
    ("view3d.select_circle", {"type": 'C', "value": 'PRESS'}, None),
    ("view3d.clip_border", {"type": 'B', "value": 'PRESS', "alt": True}, None),
    ("view3d.zoom_border", {"type": 'B', "value": 'PRESS', "shift": True}, None),
    ("view3d.render_border", {"type": 'B', "value": 'PRESS', "ctrl": True}, None),
    ("view3d.clear_render_border", {"type": 'B', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("view3d.camera_to_view", {"type": 'NUMPAD_0', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("view3d.object_as_camera", {"type": 'NUMPAD_0', "value": 'PRESS', "ctrl": True}, None),
    ("view3d.copybuffer", {"type": 'C', "value": 'PRESS', "ctrl": True}, None),
    ("view3d.pastebuffer", {"type": 'V', "value": 'PRESS', "ctrl": True}, None),
    ("wm.context_toggle",
     {"type": 'TAB', "value": 'PRESS', "shift": True},
     {"properties":
      [("data_path", 'tool_settings.use_snap'),
       ],
      },
     ),
    ("wm.call_panel",
     {"type": 'TAB', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("name", 'VIEW3D_PT_snapping'),
       ("keep_open", True),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'S', "value": 'PRESS', "shift": True},
     {"properties":
      [("name", 'VIEW3D_MT_snap_pie'),
       ],
      },
     ),
    ("wm.context_toggle",
     {"type": 'ACCENT_GRAVE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("data_path", 'space_data.show_gizmo'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'PERIOD', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_pivot_pie'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'COMMA', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_orientations_pie'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'Z', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_MT_shading_pie'),
       ],
      },
     ),
    ("view3d.toggle_shading",
     {"type": 'Z', "value": 'PRESS', "shift": True},
     {"properties":
      [("type", 'WIREFRAME'),
       ],
      },
     ),
    ("view3d.toggle_xray", {"type": 'Z', "value": 'PRESS', "alt": True}, None),
    ("wm.context_toggle",
     {"type": 'Z', "value": 'PRESS', "shift": True, "alt": True},
     {"properties":
      [("data_path", 'space_data.overlay.show_overlays'),
       ],
      },
     ),
    ("wm.tool_set_by_id",
     {"type": 'W', "value": 'PRESS'},
     {"properties":
      [("name", 'builtin.select_box'),
       ("cycle", True),
       ],
      },
     ),
    ],
   },
  ),
 ("Image",
  {"space_type": 'IMAGE_EDITOR', "region_type": 'WINDOW'},
  {"items":
   [("wm.call_menu_pie",
     {"type": 'TAB', "value": 'PRESS'},
     {"properties":
      [("name", 'MACHIN3_MT_modes_pie'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'TAB', "value": 'PRESS'},
     {"properties":
      [("name", 'MACHIN3_MT_modes_pie'),
       ],
      },
     ),
    ("image.view_all", {"type": 'HOME', "value": 'PRESS'}, None),
    ("image.view_all",
     {"type": 'HOME', "value": 'PRESS', "shift": True},
     {"properties":
      [("fit_view", True),
       ],
      },
     ),
    ("image.view_selected", {"type": 'NUMPAD_PERIOD', "value": 'PRESS'}, None),
    ("image.view_cursor_center", {"type": 'C', "value": 'PRESS', "shift": True}, None),
    ("image.view_pan", {"type": 'MIDDLEMOUSE', "value": 'PRESS'}, None),
    ("image.view_pan", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "shift": True}, None),
    ("image.view_pan", {"type": 'TRACKPADPAN', "value": 'ANY'}, None),
    ("image.view_all", {"type": 'NDOF_BUTTON_FIT', "value": 'PRESS'}, None),
    ("image.view_ndof", {"type": 'NDOF_MOTION', "value": 'ANY'}, None),
    ("image.view_zoom_in", {"type": 'WHEELINMOUSE', "value": 'PRESS'}, None),
    ("image.view_zoom_out", {"type": 'WHEELOUTMOUSE', "value": 'PRESS'}, None),
    ("image.view_zoom_in", {"type": 'NUMPAD_PLUS', "value": 'PRESS', "repeat": True}, None),
    ("image.view_zoom_out", {"type": 'NUMPAD_MINUS', "value": 'PRESS', "repeat": True}, None),
    ("image.view_zoom", {"type": 'MIDDLEMOUSE', "value": 'PRESS', "ctrl": True}, None),
    ("image.view_zoom", {"type": 'TRACKPADZOOM', "value": 'ANY'}, None),
    ("image.view_zoom", {"type": 'TRACKPADPAN', "value": 'ANY', "ctrl": True}, None),
    ("image.view_zoom_border", {"type": 'B', "value": 'PRESS', "shift": True}, None),
    ("image.view_zoom_ratio",
     {"type": 'NUMPAD_8', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("ratio", 8.0),
       ],
      },
     ),
    ("image.view_zoom_ratio",
     {"type": 'NUMPAD_4', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("ratio", 4.0),
       ],
      },
     ),
    ("image.view_zoom_ratio",
     {"type": 'NUMPAD_2', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("ratio", 2.0),
       ],
      },
     ),
    ("image.view_zoom_ratio",
     {"type": 'NUMPAD_8', "value": 'PRESS', "shift": True},
     {"properties":
      [("ratio", 8.0),
       ],
      },
     ),
    ("image.view_zoom_ratio",
     {"type": 'NUMPAD_4', "value": 'PRESS', "shift": True},
     {"properties":
      [("ratio", 4.0),
       ],
      },
     ),
    ("image.view_zoom_ratio",
     {"type": 'NUMPAD_2', "value": 'PRESS', "shift": True},
     {"properties":
      [("ratio", 2.0),
       ],
      },
     ),
    ("image.view_zoom_ratio",
     {"type": 'NUMPAD_1', "value": 'PRESS'},
     {"properties":
      [("ratio", 1.0),
       ],
      },
     ),
    ("image.view_zoom_ratio",
     {"type": 'NUMPAD_2', "value": 'PRESS'},
     {"properties":
      [("ratio", 0.5),
       ],
      },
     ),
    ("image.view_zoom_ratio",
     {"type": 'NUMPAD_4', "value": 'PRESS'},
     {"properties":
      [("ratio", 0.25),
       ],
      },
     ),
    ("image.view_zoom_ratio",
     {"type": 'NUMPAD_8', "value": 'PRESS'},
     {"properties":
      [("ratio", 0.125),
       ],
      },
     ),
    ("image.change_frame", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
    ("image.sample", {"type": 'RIGHTMOUSE', "value": 'PRESS'}, None),
    ("image.curves_point_set",
     {"type": 'RIGHTMOUSE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("point", 'BLACK_POINT'),
       ],
      },
     ),
    ("image.curves_point_set",
     {"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True},
     {"properties":
      [("point", 'WHITE_POINT'),
       ],
      },
     ),
    ("object.mode_set",
     {"type": 'TAB', "value": 'PRESS'},
     {"properties":
      [("mode", 'EDIT'),
       ("toggle", True),
       ],
      },
     ),
    ("wm.context_set_int",
     {"type": 'ONE', "value": 'PRESS'},
     {"properties":
      [("data_path", 'space_data.image.render_slots.active_index'),
       ("value", 0),
       ],
      },
     ),
    ("wm.context_set_int",
     {"type": 'TWO', "value": 'PRESS'},
     {"properties":
      [("data_path", 'space_data.image.render_slots.active_index'),
       ("value", 1),
       ],
      },
     ),
    ("wm.context_set_int",
     {"type": 'THREE', "value": 'PRESS'},
     {"properties":
      [("data_path", 'space_data.image.render_slots.active_index'),
       ("value", 2),
       ],
      },
     ),
    ("wm.context_set_int",
     {"type": 'FOUR', "value": 'PRESS'},
     {"properties":
      [("data_path", 'space_data.image.render_slots.active_index'),
       ("value", 3),
       ],
      },
     ),
    ("wm.context_set_int",
     {"type": 'FIVE', "value": 'PRESS'},
     {"properties":
      [("data_path", 'space_data.image.render_slots.active_index'),
       ("value", 4),
       ],
      },
     ),
    ("wm.context_set_int",
     {"type": 'SIX', "value": 'PRESS'},
     {"properties":
      [("data_path", 'space_data.image.render_slots.active_index'),
       ("value", 5),
       ],
      },
     ),
    ("wm.context_set_int",
     {"type": 'SEVEN', "value": 'PRESS'},
     {"properties":
      [("data_path", 'space_data.image.render_slots.active_index'),
       ("value", 6),
       ],
      },
     ),
    ("wm.context_set_int",
     {"type": 'EIGHT', "value": 'PRESS'},
     {"properties":
      [("data_path", 'space_data.image.render_slots.active_index'),
       ("value", 7),
       ],
      },
     ),
    ("wm.context_set_int",
     {"type": 'NINE', "value": 'PRESS'},
     {"properties":
      [("data_path", 'space_data.image.render_slots.active_index'),
       ("value", 8),
       ],
      },
     ),
    ("image.render_border", {"type": 'B', "value": 'PRESS', "ctrl": True}, None),
    ("image.clear_render_border", {"type": 'B', "value": 'PRESS', "ctrl": True, "alt": True}, None),
    ("wm.context_toggle",
     {"type": 'ACCENT_GRAVE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("data_path", 'space_data.show_gizmo'),
       ],
      },
     ),
    ("wm.context_toggle",
     {"type": 'Z', "value": 'PRESS', "shift": True, "alt": True},
     {"properties":
      [("data_path", 'space_data.overlay.show_overlays'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'RIGHTMOUSE', "value": 'PRESS'},
     {"properties":
      [("name", 'IMAGE_MT_mask_context_menu'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'APP', "value": 'PRESS'},
     {"properties":
      [("name", 'IMAGE_MT_mask_context_menu'),
       ],
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'PERIOD', "value": 'PRESS'},
     {"properties":
      [("name", 'IMAGE_MT_pivot_pie'),
       ],
      },
     ),
    ("image.view_pan", {"type": 'LEFTMOUSE', "value": 'CLICK_DRAG', "shift": True, "alt": True}, None),
    ("image.view_zoom", {"type": 'LEFTMOUSE', "value": 'CLICK_DRAG', "ctrl": True, "alt": True}, None),
    ],
   },
  ),
 ("Image Paint",
  {"space_type": 'EMPTY', "region_type": 'WINDOW'},
  {"items":
   [("paint.image_paint", {"type": 'LEFTMOUSE', "value": 'PRESS'}, None),
    ("paint.image_paint",
     {"type": 'LEFTMOUSE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("mode", 'INVERT'),
       ],
      },
     ),
    ("paint.image_paint",
     {"type": 'LEFTMOUSE', "value": 'PRESS', "shift": True},
     {"properties":
      [("mode", 'SMOOTH'),
       ],
      },
     ),
    ("paint.brush_colors_flip", {"type": 'X', "value": 'PRESS'}, None),
    ("paint.grab_clone", {"type": 'RIGHTMOUSE', "value": 'PRESS'}, None),
    ("paint.sample_color", {"type": 'X', "value": 'PRESS', "shift": True}, None),
    ("brush.scale_size",
     {"type": 'LEFT_BRACKET', "value": 'PRESS', "repeat": True},
     {"properties":
      [("scalar", 0.9),
       ],
      },
     ),
    ("brush.scale_size",
     {"type": 'RIGHT_BRACKET', "value": 'PRESS', "repeat": True},
     {"properties":
      [("scalar", 1.1111112),
       ],
      },
     ),
    ("wm.radial_control",
     {"type": 'F', "value": 'PRESS'},
     {"properties":
      [("data_path_primary", 'tool_settings.image_paint.brush.size'),
       ("data_path_secondary", 'tool_settings.unified_paint_settings.size'),
       ("use_secondary", 'tool_settings.unified_paint_settings.use_unified_size'),
       ("rotation_path", 'tool_settings.image_paint.brush.mask_texture_slot.angle'),
       ("color_path", 'tool_settings.image_paint.brush.cursor_color_add'),
       ("fill_color_path", 'tool_settings.image_paint.brush.color'),
       ("fill_color_override_path", 'tool_settings.unified_paint_settings.color'),
       ("fill_color_override_test_path", 'tool_settings.unified_paint_settings.use_unified_color'),
       ("zoom_path", 'space_data.zoom'),
       ("image_id", 'tool_settings.image_paint.brush'),
       ("secondary_tex", True),
       ],
      },
     ),
    ("wm.radial_control",
     {"type": 'F', "value": 'PRESS', "shift": True},
     {"properties":
      [("data_path_primary", 'tool_settings.image_paint.brush.strength'),
       ("data_path_secondary", 'tool_settings.unified_paint_settings.strength'),
       ("use_secondary", 'tool_settings.unified_paint_settings.use_unified_strength'),
       ("rotation_path", 'tool_settings.image_paint.brush.mask_texture_slot.angle'),
       ("color_path", 'tool_settings.image_paint.brush.cursor_color_add'),
       ("fill_color_path", 'tool_settings.image_paint.brush.color'),
       ("fill_color_override_path", 'tool_settings.unified_paint_settings.color'),
       ("fill_color_override_test_path", 'tool_settings.unified_paint_settings.use_unified_color'),
       ("zoom_path", ''),
       ("image_id", 'tool_settings.image_paint.brush'),
       ("secondary_tex", True),
       ],
      },
     ),
    ("wm.radial_control",
     {"type": 'F', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("data_path_primary", 'tool_settings.image_paint.brush.texture_slot.angle'),
       ("data_path_secondary", ''),
       ("use_secondary", ''),
       ("rotation_path", 'tool_settings.image_paint.brush.texture_slot.angle'),
       ("color_path", 'tool_settings.image_paint.brush.cursor_color_add'),
       ("fill_color_path", 'tool_settings.image_paint.brush.color'),
       ("fill_color_override_path", 'tool_settings.unified_paint_settings.color'),
       ("fill_color_override_test_path", 'tool_settings.unified_paint_settings.use_unified_color'),
       ("zoom_path", ''),
       ("image_id", 'tool_settings.image_paint.brush'),
       ("secondary_tex", False),
       ],
      },
     ),
    ("wm.radial_control",
     {"type": 'F', "value": 'PRESS', "ctrl": True, "alt": True},
     {"properties":
      [("data_path_primary", 'tool_settings.image_paint.brush.mask_texture_slot.angle'),
       ("data_path_secondary", ''),
       ("use_secondary", ''),
       ("rotation_path", 'tool_settings.image_paint.brush.mask_texture_slot.angle'),
       ("color_path", 'tool_settings.image_paint.brush.cursor_color_add'),
       ("fill_color_path", 'tool_settings.image_paint.brush.color'),
       ("fill_color_override_path", 'tool_settings.unified_paint_settings.color'),
       ("fill_color_override_test_path", 'tool_settings.unified_paint_settings.use_unified_color'),
       ("zoom_path", ''),
       ("image_id", 'tool_settings.image_paint.brush'),
       ("secondary_tex", True),
       ],
      },
     ),
    ("brush.stencil_control",
     {"type": 'RIGHTMOUSE', "value": 'PRESS'},
     {"properties":
      [("mode", 'TRANSLATION'),
       ],
      },
     ),
    ("brush.stencil_control",
     {"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True},
     {"properties":
      [("mode", 'SCALE'),
       ],
      },
     ),
    ("brush.stencil_control",
     {"type": 'RIGHTMOUSE', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("mode", 'ROTATION'),
       ],
      },
     ),
    ("brush.stencil_control",
     {"type": 'RIGHTMOUSE', "value": 'PRESS', "alt": True},
     {"properties":
      [("mode", 'TRANSLATION'),
       ("texmode", 'SECONDARY'),
       ],
      },
     ),
    ("brush.stencil_control",
     {"type": 'RIGHTMOUSE', "value": 'PRESS', "shift": True, "alt": True},
     {"properties":
      [("mode", 'SCALE'),
       ("texmode", 'SECONDARY'),
       ],
      },
     ),
    ("brush.stencil_control",
     {"type": 'RIGHTMOUSE', "value": 'PRESS', "ctrl": True, "alt": True},
     {"properties":
      [("mode", 'ROTATION'),
       ("texmode", 'SECONDARY'),
       ],
      },
     ),
    ("wm.context_toggle",
     {"type": 'ONE', "value": 'PRESS'},
     {"properties":
      [("data_path", 'image_paint_object.data.use_paint_mask'),
       ],
      },
     ),
    ("wm.context_toggle",
     {"type": 'S', "value": 'PRESS', "shift": True},
     {"properties":
      [("data_path", 'tool_settings.image_paint.brush.use_smooth_stroke'),
       ],
      },
     ),
    ("wm.context_menu_enum",
     {"type": 'E', "value": 'PRESS', "alt": True},
     {"properties":
      [("data_path", 'tool_settings.image_paint.brush.stroke_method'),
       ],
      },
     ),
    ("wm.call_panel",
     {"type": 'RIGHTMOUSE', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_PT_paint_texture_context_menu'),
       ],
      },
     ),
    ("wm.call_panel",
     {"type": 'APP', "value": 'PRESS'},
     {"properties":
      [("name", 'VIEW3D_PT_paint_texture_context_menu'),
       ],
      },
     ),
    ("paint.sample_color",
     {"type": 'LEFTMOUSE', "value": 'PRESS', "alt": True},
     {"properties":
      [("palette", True),
       ],
      },
     ),
    ],
   },
  ),
 ("Toolbar Popup <temp>",
  {"space_type": 'EMPTY', "region_type": 'TEMPORARY'},
  {"items":
   [("wm.tool_set_by_id",
     {"type": 'D', "value": 'PRESS'},
     {"properties":
      [("name", 'builtin.annotate'),
       ],
      },
     ),
    ],
   },
  ),
 ("Window",
  {"space_type": 'EMPTY', "region_type": 'WINDOW'},
  {"items":
   [("machin3.save_versioned_startup_file",
     {"type": 'U', "value": 'PRESS', "ctrl": True},
     {    "active":False,
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'S', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("name", 'MACHIN3_MT_save_pie'),
       ],
      },
     ),
    ("machin3.save_versioned_startup_file",
     {"type": 'U', "value": 'PRESS', "ctrl": True},
     {    "active":False,
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'S', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("name", 'MACHIN3_MT_save_pie'),
       ],
      },
     ),
    ("machin3.save_versioned_startup_file",
     {"type": 'U', "value": 'PRESS', "ctrl": True},
     {    "active":False,
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'S', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("name", 'MACHIN3_MT_save_pie'),
       ],
      },
     ),
    ("machin3.save_versioned_startup_file",
     {"type": 'U', "value": 'PRESS', "ctrl": True},
     {    "active":False,
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'S', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("name", 'MACHIN3_MT_save_pie'),
       ],
      },
     ),
    ("machin3.save_versioned_startup_file",
     {"type": 'U', "value": 'PRESS', "ctrl": True},
     {    "active":False,
      },
     ),
    ("wm.call_menu_pie",
     {"type": 'S', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("name", 'MACHIN3_MT_save_pie'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'N', "value": 'PRESS', "ctrl": True},
     {"properties":
      [("name", 'TOPBAR_MT_file_new'),
       ],
      },
     ),
    ("wm.call_menu",
     {"type": 'O', "value": 'PRESS', "shift": True, "ctrl": True},
     {"properties":
      [("name", 'TOPBAR_MT_file_open_recent'),
       ],
      },
     ),
    ("wm.open_mainfile", {"type": 'O', "value": 'PRESS', "ctrl": True}, None),
    ("wm.save_mainfile", {"type": 'S', "value": 'PRESS', "ctrl": True}, None),
    ("wm.save_as_mainfile", {"type": 'S', "value": 'PRESS', "shift": True, "ctrl": True}, None),
    ("wm.save_mainfile",
     {"type": 'S', "value": 'PRESS', "ctrl": True, "alt": True},
     {"properties":
      [("incremental", True),
       ],
      },
     ),
    ("wm.quit_blender", {"type": 'Q', "value": 'PRESS', "ctrl": True}, None),
    ("wm.call_menu",
     {"type": 'Q', "value": 'PRESS'},
     {"properties":
      [("name", 'SCREEN_MT_user_menu'),
       ],
      },
     ),
    ("screen.space_type_set_or_cycle",
     {"type": 'F1', "value": 'PRESS', "shift": True},
     {"properties":
      [("space_type", 'FILE_BROWSER'),
       ],
      },
     ),
    ("screen.space_type_set_or_cycle",
     {"type": 'F2', "value": 'PRESS', "shift": True},
     {"properties":
      [("space_type", 'CLIP_EDITOR'),
       ],
      },
     ),
    ("screen.space_type_set_or_cycle",
     {"type": 'F3', "value": 'PRESS', "shift": True},
     {"properties":
      [("space_type", 'NODE_EDITOR'),
       ],
      },
     ),
    ("screen.space_type_set_or_cycle",
     {"type": 'F4', "value": 'PRESS', "shift": True},
     {"properties":
      [("space_type", 'CONSOLE'),
       ],
      },
     ),
    ("screen.space_type_set_or_cycle",
     {"type": 'F5', "value": 'PRESS', "shift": True},
     {"properties":
      [("space_type", 'VIEW_3D'),
       ],
      },
     ),
    ("screen.space_type_set_or_cycle",
     {"type": 'F6', "value": 'PRESS', "shift": True},
     {"properties":
      [("space_type", 'GRAPH_EDITOR'),
       ],
      },
     ),
    ("screen.space_type_set_or_cycle",
     {"type": 'F7', "value": 'PRESS', "shift": True},
     {"properties":
      [("space_type", 'PROPERTIES'),
       ],
      },
     ),
    ("screen.space_type_set_or_cycle",
     {"type": 'F8', "value": 'PRESS', "shift": True},
     {"properties":
      [("space_type", 'SEQUENCE_EDITOR'),
       ],
      },
     ),
    ("screen.space_type_set_or_cycle",
     {"type": 'F9', "value": 'PRESS', "shift": True},
     {"properties":
      [("space_type", 'OUTLINER'),
       ],
      },
     ),
    ("screen.space_type_set_or_cycle",
     {"type": 'F10', "value": 'PRESS', "shift": True},
     {"properties":
      [("space_type", 'IMAGE_EDITOR'),
       ],
      },
     ),
    ("screen.space_type_set_or_cycle",
     {"type": 'F11', "value": 'PRESS', "shift": True},
     {"properties":
      [("space_type", 'TEXT_EDITOR'),
       ],
      },
     ),
    ("screen.space_type_set_or_cycle",
     {"type": 'F12', "value": 'PRESS', "shift": True},
     {"properties":
      [("space_type", 'DOPESHEET_EDITOR'),
       ],
      },
     ),
    ("wm.call_panel",
     {"type": 'NDOF_BUTTON_MENU', "value": 'PRESS'},
     {"properties":
      [("name", 'USERPREF_PT_ndof_settings'),
       ],
      },
     ),
    ("wm.context_scale_float",
     {"type": 'NDOF_BUTTON_PLUS', "value": 'PRESS'},
     {"properties":
      [("data_path", 'preferences.inputs.ndof_sensitivity'),
       ("value", 1.1),
       ],
      },
     ),
    ("wm.context_scale_float",
     {"type": 'NDOF_BUTTON_MINUS', "value": 'PRESS'},
     {"properties":
      [("data_path", 'preferences.inputs.ndof_sensitivity'),
       ("value", 0.90909094),
       ],
      },
     ),
    ("wm.context_scale_float",
     {"type": 'NDOF_BUTTON_PLUS', "value": 'PRESS', "shift": True},
     {"properties":
      [("data_path", 'preferences.inputs.ndof_sensitivity'),
       ("value", 1.5),
       ],
      },
     ),
    ("wm.context_scale_float",
     {"type": 'NDOF_BUTTON_MINUS', "value": 'PRESS', "shift": True},
     {"properties":
      [("data_path", 'preferences.inputs.ndof_sensitivity'),
       ("value", 0.6666667),
       ],
      },
     ),
    ("info.reports_display_update", {"type": 'TIMER_REPORT', "value": 'ANY', "any": True}, None),
    ("wm.doc_view_manual_ui_context", {"type": 'F1', "value": 'PRESS'}, None),
    ("wm.call_panel",
     {"type": 'F2', "value": 'PRESS'},
     {"properties":
      [("name", 'TOPBAR_PT_name'),
       ("keep_open", False),
       ],
      },
     ),
    ("wm.batch_rename", {"type": 'F2', "value": 'PRESS', "ctrl": True}, None),
    ("wm.search_menu", {"type": 'F3', "value": 'PRESS'}, None),
    ("wm.call_menu",
     {"type": 'F4', "value": 'PRESS'},
     {"properties":
      [("name", 'TOPBAR_MT_file_context_menu'),
       ],
      },
     ),
    ("wm.toolbar_fallback_pie", {"type": 'W', "value": 'PRESS', "alt": True}, None),
    ("wm.toolbar_prompt", {"type": 'LEFT_ALT', "value": 'CLICK'}, None),
    ("wm.toolbar_prompt", {"type": 'RIGHT_ALT', "value": 'CLICK'}, None),
    ("wm.search_menu", {"type": 'SPACE', "value": 'PRESS'}, None),
    ("wm.context_toggle",
     {"type": 'D', "value": 'PRESS', "repeat": True},
     {"properties":
      [("data_path", 'scene.tool_settings.use_transform_data_origin'),
       ],
      },
     ),
    ],
   },
  ),
 ]


if __name__ == "__main__":
    # Only add keywords that are supported.
    from bpy.app import version as blender_version
    keywords = {}
    if blender_version >= (2, 92, 0):
        keywords["keyconfig_version"] = keyconfig_version
    import os
    from bl_keymap_utils.io import keyconfig_import_from_data
    keyconfig_import_from_data(
        os.path.splitext(os.path.basename(__file__))[0],
        keyconfig_data,
        **keywords,
    )
